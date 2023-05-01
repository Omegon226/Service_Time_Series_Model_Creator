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
file_handler = logging.FileHandler("app/logs/scripts.data_create_param.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class DataCreatorParam:
    @staticmethod
    def add_new_column(time_series_df: TimeSeriesDF, type_of_param: str, window_size: int):
        logger.info(f"Создание нового параметра для существующих данных")

        try:
            timer_start: float = perf_counter()
            if type_of_param == "mean":
                time_series_df.df_work["Mean"] = time_series_df.df_work.mean(axis=1)
            elif type_of_param == "median":
                time_series_df.df_work["Median"] = time_series_df.df_work.median(axis=1)
            elif type_of_param == "range":
                time_series_df.df_work["Range"] = time_series_df.df_work.max(axis=1) - time_series_df.df_work.min(axis=1)
            elif type_of_param == "std":
                time_series_df.df_work["STD"] = time_series_df.df_work.std(axis=1)
            elif type_of_param == "rolling mean":
                if window_size is None:
                    error_message = "Не было указан размер окна для добавления новых данных"
                    raise Exception(error_message)
                if time_series_df.main_parameter is None:
                    error_message = "Для создания такого параметра нужно знать влияющий параметр"
                    raise Exception(error_message)

                time_series_df.df_work[f"Rolling Mean {time_series_df.main_parameter}"] = \
                    time_series_df.df_work[time_series_df.main_parameter].rolling(
                        window=window_size).mean()
            elif type_of_param == "rolling median":
                if window_size is None:
                    error_message = "Не было указан размер окна для добавления новых данных"
                    raise Exception(error_message)
                if time_series_df.main_parameter is None:
                    error_message = "Для создания такого параметра нужно знать влияющий параметр"
                    raise Exception(error_message)

                time_series_df.df_work[f"Rolling Median {time_series_df.main_parameter}"] = \
                    time_series_df.df_work[time_series_df.main_parameter].rolling(
                        window=window_size).median()
            elif type_of_param == "rolling range":
                if window_size is None:
                    error_message = "Не было указан размер окна для добавления новых данных"
                    raise Exception(error_message)
                if time_series_df.main_parameter is None:
                    error_message = "Для создания такого параметра нужно знать влияющий параметр"
                    raise Exception(error_message)

                time_series_df.df_work[f"Rolling Range {time_series_df.main_parameter}"] = \
                    time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).max() - \
                    time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).min()
            elif type_of_param == "rolling std":
                if window_size is None:
                    error_message = "Не было указан размер окна для добавления новых данных"
                    raise Exception(error_message)
                if time_series_df.main_parameter is None:
                    error_message = "Для создания такого параметра нужно знать влияющий параметр"
                    raise Exception(error_message)

                time_series_df.df_work[f"Rolling STD {time_series_df.main_parameter}"] = \
                    time_series_df.df_work[time_series_df.main_parameter].rolling(
                        window=window_size).std()
            else:
                error_message = f"Переданный тип параметра ({type_of_param}) для создания нового параметра не существует"
                raise Exception(error_message)
            timer_end: float = perf_counter()

            logger.info(f"Новый параметр (type_of_param) был успешно создан! "
                        f"Затрачено времени: {timer_end - timer_start}")
            logger.debug(f"Новый временной ряд: {time_series_df.df_work}")

            return time_series_df
        except Exception as error:
            error_message: str = f"Произошла ошибка при создании нового параметра временного ряда"
            http_error(error_message, error, logger=logger)

