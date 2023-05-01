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
file_handler = logging.FileHandler("app/logs/scripts.data_change_main_param.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class SetterOfMainParameter:
    @staticmethod
    def set_main_parameter(time_series_df: TimeSeriesDF, parameter_to_set_main: str):
        logger.info(f"Установка параметра: {parameter_to_set_main}, как главного для временных рядов")
        params_of_df = list(time_series_df.df_work.columns)
        if parameter_to_set_main in params_of_df:
            time_series_df.main_parameter = [parameter_to_set_main]
            return time_series_df
        else:
            error_message: str = f"В данных о временных рядах нету такого параметра: {parameter_to_set_main}"
            http_error(error_message, logger=logger)
