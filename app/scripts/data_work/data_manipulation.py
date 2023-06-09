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
    def get_full_data_frame(time_series_df: TimeSeriesDF):
        logger.info(f"Получение всех данных временных рядов")

        try:
            timer_start: float = perf_counter()
            data = time_series_df.df_work.to_dict()
            timer_end: float = perf_counter()

            logger.info(f"Получение всех данных временных рядов прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            logger.debug(f"data: {data}")
            return data
        except Exception as error:
            error_message: str = f"Произошла ошибка при получение всех данных временных рядов"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def get_all_params(time_series_df: TimeSeriesDF):
        logger.info(f"Получение всех параметров временного ряда")

        try:
            timer_start: float = perf_counter()
            params = time_series_df.df_work.columns.tolist()
            timer_end: float = perf_counter()

            logger.info(f"Получение всех параметров прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            logger.debug(f"params: {params}")
            return params
        except Exception as error:
            error_message: str = f"Произошла ошибка при получение всех параметров временного ряда"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def get_main_param(time_series_df: TimeSeriesDF):
        logger.info(f"Получение основного параметра временного ряда")

        try:
            timer_start: float = perf_counter()
            main_parameter = time_series_df.main_parameter
            timer_end: float = perf_counter()

            logger.info(f"Получение основного параметра прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            logger.debug(f"main_parameter: {main_parameter}")
            return main_parameter
        except Exception as error:
            error_message: str = f"Произошла ошибка при получении основного параметра временного ряда"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def get_data_params(time_series_df: TimeSeriesDF):
        logger.info(f"Получение всех параметров для данных временного ряда")

        try:
            timer_start: float = perf_counter()
            data_params = time_series_df.data_params
            timer_end: float = perf_counter()

            logger.info(f"Получение всех параметров для данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            logger.debug(f"params: {data_params}")
            return data_params
        except Exception as error:
            error_message: str = f"Произошла ошибка при получение всех параметров для данных временного ряда"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def get_statistics_of_time_series(time_series_df: TimeSeriesDF, params_statistics: list | str):
        logger.info(f"Получение статистических данных о временном ряде")

        try:
            timer_start: float = perf_counter()
            description = time_series_df.df_work[params_statistics].describe().to_dict()
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
            if time_series_df.main_parameter in columns_to_drop or \
                    time_series_df.main_parameter == columns_to_drop:
                raise Exception("Влияющий параметр не может быть удалён. Если он вам не нужен, то замените его")

            timer_start: float = perf_counter()
            time_series_df.df_work = time_series_df.df_work.drop(columns=columns_to_drop)
            if type(columns_to_drop) is str:
                time_series_df.data_params.remove(columns_to_drop)
            elif type(columns_to_drop) is list:
                for i in columns_to_drop:
                    time_series_df.data_params.remove(i)
            timer_end: float = perf_counter()

            logger.info(f"В результате работы были успешно удалена/ы колонка/и {columns_to_drop} "
                        f"Затрачено времени: {timer_end - timer_start}")

            return time_series_df
        except Exception as error:
            error_message: str = f"В результате удаления параметров произошла ошибка"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def change_data_params(time_series_df: TimeSeriesDF, new_data_params: list):
        logger.info(f"Установка параметров: {new_data_params}, как данные для создания новых параметров")

        try:
            if not set(new_data_params).issubset(time_series_df.df_work.columns):
                raise Exception(f"Не хватает параметров: {set(new_data_params) - set(time_series_df.df_work.columns)}")

            timer_start: float = perf_counter()
            time_series_df.data_params = new_data_params
            timer_end: float = perf_counter()

            logger.info(f"В результате работы были успешно заменены параметры данных {new_data_params} "
                        f"Затрачено времени: {timer_end - timer_start}")

            return time_series_df
        except Exception as error:
            error_message: str = f"В результате заменены параметров данных произошла ошибка"
            http_error(error_message, error, logger=logger)
