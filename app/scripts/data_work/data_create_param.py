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
    def add_new_column(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None,
                       window_size: int):
        logger.info(f"Создание нового параметра для существующих данных. "
                    f"На основе параметров: {time_series_df.data_params} "
                    f"Внимание! "
                    f"Параметры создаются на основе параметров, которые указаны, как параметры данных (data_params)")

        try:
            timer_start: float = perf_counter()
            if type_of_param == "mean":
                time_series_df = DataCreatorParam._add_mean(time_series_df, type_of_param, name_of_new_param)
            elif type_of_param == "median":
                time_series_df = DataCreatorParam._add_median(time_series_df, type_of_param, name_of_new_param)
            elif type_of_param == "range":
                time_series_df = DataCreatorParam._add_range(time_series_df, type_of_param, name_of_new_param)
            elif type_of_param == "std":
                time_series_df = DataCreatorParam._add_std(time_series_df, type_of_param, name_of_new_param)
            elif type_of_param == "rolling mean":
                time_series_df = DataCreatorParam._add_rolling_mean(time_series_df, type_of_param, name_of_new_param,
                                                                    window_size)
            elif type_of_param == "rolling median":
                time_series_df = DataCreatorParam._add_rolling_median(time_series_df, type_of_param, name_of_new_param,
                                                                      window_size)
            elif type_of_param == "rolling range":
                time_series_df = DataCreatorParam._add_rolling_range(time_series_df, type_of_param, name_of_new_param,
                                                                     window_size)
            elif type_of_param == "rolling std":
                time_series_df = DataCreatorParam._add_rolling_std(time_series_df, type_of_param, name_of_new_param,
                                                                   window_size)
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

    @staticmethod
    def _add_mean(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "Mean"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[time_series_df.data_params].mean(axis=1)
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param}]
        return time_series_df

    @staticmethod
    def _add_median(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "Median"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[time_series_df.data_params].median(axis=1)
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param}]
        return time_series_df

    @staticmethod
    def _add_range(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "Range"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[time_series_df.data_params].max(axis=1) - \
                                                    time_series_df.df_work[time_series_df.data_params].min(axis=1)
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param}]
        return time_series_df

    @staticmethod
    def _add_std(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "STD"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[time_series_df.data_params].std(axis=1)
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param}]
        return time_series_df

    @staticmethod
    def _add_rolling_mean(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None,
                           window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling Mean {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = \
            time_series_df.df_work[time_series_df.main_parameter].rolling(
                window=window_size).mean()
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param,
                                                            "window_size": window_size}]
        return time_series_df

    @staticmethod
    def _add_rolling_median(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None,
                             window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling Median {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = \
            time_series_df.df_work[time_series_df.main_parameter].rolling(
                window=window_size).median()
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param,
                                                            "window_size": window_size}]
        return time_series_df

    @staticmethod
    def _add_rolling_range(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None,
                            window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling Range {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = \
            time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).max() - \
            time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).min()
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param,
                                                            "window_size": window_size}]
        return time_series_df

    @staticmethod
    def _add_rolling_std(time_series_df: TimeSeriesDF, type_of_param: str, name_of_new_param: str | None,
                          window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling STD {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = \
            time_series_df.df_work[time_series_df.main_parameter].rolling(
                window=window_size).std()
        # Установка данных для дальнейшего создания ColumnTransformer
        time_series_df.sequence_of_creating_new_params += [{"param": type_of_param,
                                                            "data_params": time_series_df.data_params,
                                                            "param_name": name_of_new_param,
                                                            "window_size": window_size}]
        return time_series_df

