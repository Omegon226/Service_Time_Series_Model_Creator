import logging
from time import perf_counter

from app.scripts.http_error import http_error
from app.models.scalers.column_transformer import ColumnTransformer
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


class CreatorColumnTransformer:
    @staticmethod
    def create_column_transformer(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            column_transformer = ColumnTransformer(data=time_series_df)

            timer_end: float = perf_counter()
            logger.info(f"Создание ColumnTransformer для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return column_transformer
        except Exception as error:
            error_message: str = "Произошла ошибка при создании ColumnTransformer"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def create_column_transformer_with_creating_new_columns(time_series_df: TimeSeriesDF):
        try:
            timer_start: float = perf_counter()

            column_transformer = ColumnTransformer(data=time_series_df)
            time_series_df = column_transformer.create_new_columns(time_series_df)

            timer_end: float = perf_counter()
            logger.info(f"Создание ColumnTransformer и создание новых столбцов для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return time_series_df
        except Exception as error:
            error_message: str = "Произошла ошибка при создании ColumnTransformer и новых столбцов"
            raise http_error(error_message, error, logger=logger)
