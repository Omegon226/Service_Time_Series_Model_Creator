import io
import logging
from time import perf_counter
import shutil
import os
import yaml
import pandas as pd

import app.service_global_variables.data
from app.scripts.http_error import http_error
from app.models.requests_models.set_pipeline_creation_data import SetPipelineCreationData
from app.models.scalers.column_transformer import ColumnTransformer
from app.models.scalers.scaler_base import ScalerBase
from app.models.scalers.max_abs_scaler import MaxAbsScaler
from app.models.scalers.min_max_scaler import MinMaxScaler
from app.models.scalers.standart_scaler import StandardScaler
from app.models.data_models.time_series_df import TimeSeriesDF
from app.models.ml_models.ml_model_base import MLModelBase
from app.models.ml_models.keras_dense_model import KerasDenseModel
from app.models.data_models.pipeline import Pipeline
from app.models.data_models.time_series_df import TimeSeriesDF

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.pipelines_creator.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class PipelineCreator:
    @staticmethod
    def create_pipelines(request_data: SetPipelineCreationData, time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            combinations = []
            name_of_combination = []
            app.service_global_variables.pipelines.pipelines = []

            for i in range(len(request_data.scalers)):
                for j in request_data.ml_models.keys():
                    request_data.ml_models[j]["param_for_prediction"] = time_series_df.main_parameter
                    combinations += [(request_data.scalers[i],
                                      request_data.ml_models[j])]
                    name_of_combination += [request_data.scalers[i] + "_" + j]

            for i in range(len(combinations)):
                column_transformer = ColumnTransformer(time_series_df)
                scaler = app.service_global_variables.pipelines.all_scalers[combinations[i][0]]()
                model = app.service_global_variables.pipelines.all_ml_models[combinations[i][1]["model"]](
                    **combinations[i][1])

                app.service_global_variables.pipelines.pipelines += [Pipeline(column_transformer, scaler, model)]

            tests = [app.service_global_variables.pipelines.all_tests[i] for i in request_data.tests]

            metrics_results = {}
            plots = {}
            counter = 0
            logger.info(name_of_combination)

            for files in os.listdir(r"app/resources/results_of_pipeline_creation/pipelines"):
                path = os.path.join(r"app/resources/results_of_pipeline_creation/pipelines", files)
                shutil.rmtree(path)
            for files in os.listdir(r"app/resources/results_of_pipeline_creation/test_results"):
                path = os.path.join(r"app/resources/results_of_pipeline_creation/test_results", files)
                shutil.rmtree(path)

            for pipeline in app.service_global_variables.pipelines.pipelines:
                plot, metrics = pipeline.fit(time_series_df, tests=tests)
                metrics_results[name_of_combination[counter]] = metrics
                plots[name_of_combination[counter]] = plot

                PipelineCreator.__save_metrics(
                    plot=plot,
                    metrics=metrics,
                    path=os.path.join(r"app/resources/results_of_pipeline_creation/test_results", f"{name_of_combination[counter]}")
                )
                pipeline.save(path=r"app/resources/results_of_pipeline_creation/pipelines",
                              name=f"{name_of_combination[counter]}")
                counter += 1

            timer_end: float = perf_counter()
            logger.info(f"Создание множества Pipeline-ов прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")

        except Exception as error:
            error_message: str = "Произошла ошибка при создании множества Pipeline-ов"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def __save_metrics(plot, metrics, path):
        os.mkdir(path)
        with open(os.path.join(path, 'metrics.yaml'), 'w+') as file:
            yaml.dump(metrics, file)
        with open(os.path.join(path, "prediction.png"), "wb+") as file:
            plot.seek(0)
            file.write(plot.read())

    @staticmethod
    def get_best_pipelines(amount: int):
        try:
            timer_start: float = perf_counter()

            metrics = {}
            path_to_result_models = r"app/resources/results_of_pipeline_creation/test_results"
            for dir_of_model in os.listdir(path_to_result_models):
                with open(os.path.join(path_to_result_models, dir_of_model, 'metrics.yaml'), 'r+') as file:
                    metrics[dir_of_model] = yaml.load(file, Loader=yaml.loader.SafeLoader)

            df_metrics = pd.DataFrame(metrics).T
            df_metrics = df_metrics.sort_values(by=list(df_metrics.columns))

            df_best_models = df_metrics.iloc[:amount]

            timer_end: float = perf_counter()
            logger.info(f"Поиск лучших Pipeline-ов завершён успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")

            return df_best_models.T.to_dict()

        except Exception as error:
            error_message: str = "Произошла ошибка при поиске Pipelin-ов"
            raise http_error(error_message, error, logger=logger)

