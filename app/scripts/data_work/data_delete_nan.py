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
file_handler = logging.FileHandler("app/logs/scripts.data_delete_nan.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class DeleterOfNanValues:
    @staticmethod
    def delete_nan_values(time_series_df: TimeSeriesDF):
        logger.info(f"Удаление строчек с NaN значениями. Всего таких строчек: {time_series_df.df_work.isna().sum().sum()}")
        logger.debug(f"Сумма NaN значений по столбцам: {time_series_df.df_work.isna().sum()}")

        previous_amount_of_rows: int = time_series_df.df_work.shape[0]
        try:
            timer_start: float = perf_counter()
            time_series_df.df_work = time_series_df.df_work.dropna()
            timer_end: float = perf_counter()

            logger.info(f"В результате сброса NaN строчек было удалено строк: {previous_amount_of_rows - time_series_df.df_work.shape[0]} "
                        f"Затрачено времени: {timer_end - timer_start}")
            return time_series_df
        except Exception as error:
            error_message: str = f"В результате удаления NaN строчек произошла ошибка!"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def change_nan_values(time_series_df: TimeSeriesDF, type_of_editing: str, window_size: int | None = None):
        logger.info(f"Замена строчек с NaN значениями на статистические значения. "
                    f"Всего таких строчек: {time_series_df.df_work.isna().sum().sum()}")
        logger.debug(f"Сумма NaN значений по столбцам: {time_series_df.df_work.isna().sum()}")

        try:
            timer_start: float = perf_counter()
            if type_of_editing == "zero":
                time_series_df.df_work = time_series_df.df_work.fillna(0)
            elif type_of_editing == "mean":
                time_series_df.df_work = time_series_df.df_work.fillna(time_series_df.df_work.mean(axis=0, skipna=True))
            elif type_of_editing == "median":
                time_series_df.df_work = time_series_df.df_work.fillna(time_series_df.df_work.median(axis=0, skipna=True))
            elif type_of_editing == "rolling mean":
                if window_size is not None:
                    time_series_df.df_work = time_series_df.df_work.fillna(
                        time_series_df.df_work.rolling(window=2, min_periods=1).mean())
                else:
                    error_message = "Не было указан размер окна для обработки NaN значений"
                    raise Exception(error_message)
            elif type_of_editing == "rolling median":
                if window_size is not None:
                    time_series_df.df_work = time_series_df.df_work.fillna(
                        time_series_df.df_work.rolling(window=2, min_periods=1).median())
                else:
                    error_message = "Не было указан размер окна для обработки NaN значений"
                    raise Exception(error_message)
            else:
                error_message = f"При образовании был неверно указан способ замены NaN значений: {type_of_editing}"
                raise Exception(error_message)
            timer_end: float = perf_counter()

            logger.info(
                f"В результате сброса NaN строчек было удалено строк: '{type_of_editing}' "
                f"Всего осталось NaN значений: {time_series_df.df_work.isna().sum().sum()} "
                f"Затрачено времени: {timer_end - timer_start}")

            return time_series_df
        except Exception as error:
            error_message: str = f"В результате замены NaN строчек на значения произошла ошибка!"
            http_error(error_message, error, logger=logger)
