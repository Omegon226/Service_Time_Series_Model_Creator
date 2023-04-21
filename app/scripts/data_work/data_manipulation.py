import numpy as np
import pandas as pd

import logging
from time import perf_counter

from app.scripts.http_error import http_error
from app.models.data_models.time_series_df import TimeSeriesDF

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.data_manipulation.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class DataManipulator:
    @staticmethod
    def get_statistics_of_time_series(time_series_df: TimeSeriesDF):
        logger.info(f"Получение статистических данных о временном ряде")

        try:
            timer_start: float = perf_counter()
            description = time_series_df.df_work.describe().to_dict()
            timer_end: float = perf_counter()

            logger.info(f"Статистика о временных рядах получена успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            logger.debug(f"description: {description}")
            return description
        except Exception as error:
            error_message: str = f"Произошла ошибка при расчёте статистик временного ряда"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def drop_columns(time_series_df: TimeSeriesDF, columns_to_drop: str | list):
        logger.info(f"Удаление ненужного/ых параметра/ов {columns_to_drop} из данных о временных рядах")

        try:
            if time_series_df.influencing_parameter in columns_to_drop or \
                    time_series_df.influencing_parameter == columns_to_drop:
                raise Exception("Влияющий параметр не может быть удалён. Если он вам не нужен, то замените его")

            timer_start: float = perf_counter()
            time_series_df.df_work = time_series_df.df_work.drop(columns=columns_to_drop)
            timer_end: float = perf_counter()

            logger.info(f"В результате работы были успешно удалена/ы колонка/и {columns_to_drop} "
                        f"Затрачено времени: {timer_end - timer_start}")

            return time_series_df
        except Exception as error:
            error_message: str = f"В результате удаления параметров произошла ошибка"
            http_error(error_message, error, logger=logger)
