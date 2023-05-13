import logging
from time import perf_counter

from app.scripts.http_error import http_error
from app.models.scalers.scaler_base import ScalerBase
from app.models.scalers.max_abs_scaler import MaxAbsScaler
from app.models.scalers.min_max_scaler import MinMaxScaler
from app.models.scalers.standart_scaler import StandardScaler
from app.models.data_models.time_series_df import TimeSeriesDF

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.create_column_transformer.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class TesterCreateScalers:
    @staticmethod
    def create_max_abs_scaler_for_all_data(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            scaler: ScalerBase = MaxAbsScaler()
            scaler.fit(data=time_series_df.df_work)

            timer_end: float = perf_counter()
            logger.info(f"Создание MaxAbsScaler для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return scaler
        except Exception as error:
            error_message: str = "Произошла ошибка при создании скейлера MaxAbsScaler"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def create_min_max_scaler_for_all_data(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            scaler: ScalerBase = MinMaxScaler()
            scaler.fit(data=time_series_df.df_work)

            timer_end: float = perf_counter()
            logger.info(f"Создание MinMaxScaler для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return scaler
        except Exception as error:
            error_message: str = "Произошла ошибка при создании скейлера MinMaxScaler"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def create_standard_scaler_for_all_data(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            scaler: ScalerBase = StandardScaler()
            scaler.fit(data=time_series_df.df_work)

            timer_end: float = perf_counter()
            logger.info(f"Создание StandardScaler для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return scaler
        except Exception as error:
            error_message: str = "Произошла ошибка при создании скейлера StandardScaler"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def save_min_max_scaler(min_max_scaler: MinMaxScaler):
        try:
            timer_start: float = perf_counter()

            min_max_scaler.save()

            timer_end: float = perf_counter()
            logger.info(f"Сохранение MinMaxScaler прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
        except Exception as error:
            error_message: str = "Произошла ошибка при сохранении MinMaxScaler"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def load_min_max_scaler():
        try:
            timer_start: float = perf_counter()

            min_max_scaler = MinMaxScaler.load()

            timer_end: float = perf_counter()
            logger.info(f"Загрузка MinMaxScaler прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")

            return min_max_scaler
        except Exception as error:
            error_message: str = "Произошла ошибка при загрузке MinMaxScaler"
            raise http_error(error_message, error, logger=logger)

