from typing import BinaryIO
import numpy as np
import pandas as pd

import logging
from time import perf_counter
from io import BytesIO

from app.scripts.http_error import http_error

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.data_import.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class Importer:
    @staticmethod
    def import_data_from_csv_bytes(bytestring: bytes, sep: str, decimal: str, encoding: str):
        logger.info(f"Началась подгрузка данных из бинарной строки формата CSV")
        try:
            timer_start: float = perf_counter()
            bytestring = BytesIO(bytestring)
            df: pd.DataFrame = pd.read_csv(bytestring,
                                           sep=sep,
                                           decimal=decimal,
                                           dtype=np.float64,
                                           engine="python",
                                           encoding=encoding)
            timer_end: float = perf_counter()

            logger.info(f"Скачка данных из бинарной строки формата CSV прошла успешно! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при загрузке эталонных данных бинарной строки формата CSV"

            http_error(error_message, error, logger=logger)

    @staticmethod
    def import_data_from_json_bytes(bytestring: bytes, sep: str, decimal: str, encoding: str):
        logger.info(f"Началась подгрузка данных из бинарной строки формата JSON")
        try:
            timer_start: float = perf_counter()
            bytestring = BytesIO(bytestring)
            df: pd.DataFrame = pd.read_json(bytestring,
                                            sep=sep,
                                            decimal=decimal,
                                            dtype=np.float64,
                                            engine="python",
                                            encoding=encoding)
            timer_end: float = perf_counter()

            logger.info(f"Скачка данных из бинарной строки формата JSON прошла успешно! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при загрузке эталонных данных бинарной строки формата JSON"

            http_error(error_message, error, logger=logger)

    @staticmethod
    def import_data_from_csv(full_path: str, sep: str, decimal: str, encoding: str):
        logger.info(f"Началась подгрузка данных из CSV файла: {full_path}")
        try:
            timer_start: float = perf_counter()
            with open(full_path, "r", encoding=encoding):
                df: pd.DataFrame = pd.read_csv(full_path,
                                               sep=sep,
                                               decimal=decimal,
                                               dtype=np.float64,
                                               engine="python",
                                               encoding=encoding)
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

    @staticmethod
    def import_data_from_uploaded_csv_file(file: BinaryIO, sep: str, decimal: str, encoding: str):
        logger.info(f"Началась подгрузка данных из CSV файла, загруженный через сервис")
        try:
            timer_start: float = perf_counter()
            df: pd.DataFrame = pd.read_csv(file,
                                           sep=sep,
                                           decimal=decimal,
                                           dtype=np.float64,
                                           engine="python",
                                           encoding=encoding)
            timer_end: float = perf_counter()

            logger.info(f"Скачка данных из CSV файла прошла успешно! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при загрузке эталонных данных из CSV: "

            http_error(error_message, error, logger=logger)

    @staticmethod
    def import_data_from_uploaded_json_file(file: BinaryIO, encoding: str):
        logger.info(f"Началась подгрузка данных из JSON файла, загруженный через сервис")
        try:
            timer_start: float = perf_counter()
            df: pd.DataFrame = pd.read_json(file, encoding=encoding)
            timer_end: float = perf_counter()

            logger.info(f"Скачка данных из JSON файла прошла успешно! " +
                        f"Затраченное время: {timer_end - timer_start}")
            logger.debug(f"Данные: {df}")

            return df
        except Exception as error:
            error_message: str = "Ошибка при загрузке эталонных данных из JSON: "

            http_error(error_message, error, logger=logger)
