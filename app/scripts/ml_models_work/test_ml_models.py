import logging
from time import perf_counter

from app.scripts.http_error import http_error
from app.models.ml_models.ml_model_base import MLModelBase
from app.models.ml_models.keras_dense_model import KerasDenseModel
from app.models.data_models.time_series_df import TimeSeriesDF

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.create_ml_models.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class TesterMlModels:
    @staticmethod
    def create_dense_model():
        try:
            timer_start: float = perf_counter()

            model: MLModelBase = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10)

            timer_end: float = perf_counter()
            logger.info(f"Создание KerasDenseModel прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return model
        except Exception as error:
            error_message: str = "Произошла ошибка при создании KerasDenseModel"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def fit_dense_model(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            model: KerasDenseModel = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10)
            model.fit(time_series_df.df_work.values, return_plot=False)

            timer_end: float = perf_counter()
            logger.info(f"Создание и обучение KerasDenseModel прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
        except Exception as error:
            error_message: str = "Произошла ошибка при создании и обучении KerasDenseModel"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def fit_dense_model_and_get_plot(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            model: KerasDenseModel = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10)
            img = model.fit(time_series_df.df_work.values, return_plot=True)

            timer_end: float = perf_counter()
            logger.info(f"Создание, обучение и построение визуализации KerasDenseModel прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return img
        except Exception as error:
            error_message: str = "Произошла ошибка при создании, обучении и построение визуализации KerasDenseModel"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def predict_dense_model(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            model: MLModelBase = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10)
            result = model.predict(time_series_df.df_work.values)

            timer_end: float = perf_counter()
            logger.info(f"Прогнозирование KerasDenseModel прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return result
        except Exception as error:
            error_message: str = "Произошла ошибка при прогнозировании KerasDenseModel"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def save_dense_model():
        try:
            timer_start: float = perf_counter()

            model: MLModelBase = KerasDenseModel([100, 200], ["relu", "relu"], 5, 100, 10)
            model.save()

            timer_end: float = perf_counter()
            logger.info(f"Сохранение KerasDenseModel прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
        except Exception as error:
            error_message: str = "Произошла ошибка при сохранении KerasDenseModel"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def load_dense_model():
        try:
            timer_start: float = perf_counter()

            model: MLModelBase = KerasDenseModel.load()

            timer_end: float = perf_counter()
            logger.info(f"Загрузка KerasDenseModel прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return model
        except Exception as error:
            error_message: str = "Произошла ошибка при загрузке KerasDenseModel"
            raise http_error(error_message, error, logger=logger)
