import numpy as np
import pandas as pd

import logging
from time import perf_counter

from app.scripts.http_error import http_error

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.data_importer.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class Importer:
    @staticmethod
    def import_data_from_csv(full_path: str, sep: str, decimal: str, encoding: str):
        logger.info(f"Началась подгрузка данных из CSV файла: {full_path}")
        try:
            timer_start: float = perf_counter()
            with open(full_path, "r", encoding=encoding):
                df: pd.DataFrame = pd.read_csv(full_path, sep=sep, decimal=decimal, dtype=np.float64, engine="python")
            timer_end: float = perf_counter()

            logger.info(f"Скачка данных из CSV файла ({full_path}) прошла успешно! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при загрузке эталонных данных из CSV: " + \
                                 f"Путь: {full_path} "

            http_error(error_message, error, logger=logger)

    @staticmethod
    def import_data_from_dict(data: dict):
        logger.info(f"Началась сохранение данных из dict")
        logger.debug(f"dict: {data}")
        try:
            timer_start: float = perf_counter()
            df: pd.DataFrame = pd.DataFrame(data)
            timer_end: float = perf_counter()

            logger.info(f"Данные были преобразованы! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при преобразование данных из dict"

            http_error(error_message, error, logger=logger)

    @staticmethod
    def import_data_from_json(full_path: str, encoding: str):
        logger.info(f"Началась подгрузка данных из JSON файла: {full_path}")
        try:
            timer_start: float = perf_counter()
            with open(full_path, "r", encoding=encoding):
                df: pd.DataFrame = pd.read_json(full_path)
            timer_end: float = perf_counter()

            logger.info(f"Скачка данных из JSON файла ({full_path}) прошла успешно! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при загрузке эталонных данных из JSON: " + \
                                 f"Путь: {full_path} "

            http_error(error_message, error, logger=logger)
