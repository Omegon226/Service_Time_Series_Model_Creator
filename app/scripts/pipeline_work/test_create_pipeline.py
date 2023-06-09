import logging
from time import perf_counter

from app.scripts.http_error import http_error
from app.models.scalers.column_transformer import ColumnTransformer
from app.models.scalers.scaler_base import ScalerBase
from app.models.scalers.max_abs_scaler import MaxAbsScaler
from app.models.scalers.min_max_scaler import MinMaxScaler
from app.models.scalers.standard_scaler import StandardScaler
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
file_handler = logging.FileHandler("app/logs/scripts.test_create_pipeline.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class TesterCreatePipeline:
    @staticmethod
    def create_pipeline(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            column_transformer = ColumnTransformer(time_series_df)
            scaler = MinMaxScaler()
            model = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10, "PARAM_1")

            pipeline = Pipeline(column_transformer, scaler, model)

            timer_end: float = perf_counter()
            logger.info(f"Создание Pipeline прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return pipeline
        except Exception as error:
            error_message: str = "Произошла ошибка при создании Pipeline"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def create_and_fit_pipeline(time_series_df: TimeSeriesDF, influencing_param="PARAM_1"):
        try:
            timer_start: float = perf_counter()

            column_transformer = ColumnTransformer(time_series_df)
            scaler = MinMaxScaler()
            model = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10, influencing_param)

            pipeline = Pipeline(column_transformer, scaler, model)

            plot = pipeline.fit(time_series_df)

            timer_end: float = perf_counter()
            logger.info(f"Создание и обучение Pipeline прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return plot
        except Exception as error:
            error_message: str = "Произошла ошибка при создании и обучении Pipeline"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def create_fit_and_predict_pipeline(time_series_df: TimeSeriesDF, influencing_param="PARAM_1"):
        try:
            timer_start: float = perf_counter()

            column_transformer = ColumnTransformer(time_series_df)
            scaler = MinMaxScaler()
            model = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10, influencing_param)

            pipeline = Pipeline(column_transformer, scaler, model)

            _ = pipeline.fit(time_series_df)

            result = pipeline.predict(time_series_df)

            timer_end: float = perf_counter()
            logger.info(f"Создание, обучение и предсказание Pipeline прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return result
        except Exception as error:
            error_message: str = "Произошла ошибка при создании, обучении и предсказании Pipeline"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def save_pipeline(time_series_df: TimeSeriesDF, influencing_param="PARAM_1"):
        try:
            timer_start: float = perf_counter()

            column_transformer = ColumnTransformer(time_series_df)
            scaler = MinMaxScaler()
            model = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10, influencing_param)

            pipeline = Pipeline(column_transformer, scaler, model)
            pipeline.save()

            timer_end: float = perf_counter()
            logger.info(f"Создание и сохранение Pipeline прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
        except Exception as error:
            error_message: str = "Произошла ошибка при создании и сохранение Pipeline"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def load_pipeline():
        try:
            timer_start: float = perf_counter()

            pipeline = Pipeline.load()

            timer_end: float = perf_counter()
            logger.info(f"Создание и сохранение Pipeline прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return pipeline
        except Exception as error:
            error_message: str = "Произошла ошибка при создании и сохранении Pipeline"
            raise http_error(error_message, error, logger=logger)
