import logging
from time import perf_counter

from app.scripts.http_error import http_error
from app.models.tests.mse_test import MSETest
from app.models.tests.rmse_test import RMSETest
from app.models.tests.test_base import TestBase
from app.models.data_models.time_series_df import TimeSeriesDF

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.test_tests.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class TesterTests:
    @staticmethod
    def test_mse():
        try:
            timer_start: float = perf_counter()

            result = MSETest.calculate_metric([1, 2, 3, 4, 5, 6], [1, 3, 2, 5, 5, 6])

            timer_end: float = perf_counter()
            logger.info(f"Расчёт MSE для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return result
        except Exception as error:
            error_message: str = "Произошла ошибка при расчёте MSE"
            raise http_error(error_message, error, logger=logger)

    @staticmethod
    def test_rmse():
        try:
            timer_start: float = perf_counter()

            result = RMSETest.calculate_metric([1, 2, 3, 4, 5, 6], [1, 3, 2, 5, 5, 6])

            timer_end: float = perf_counter()
            logger.info(f"Расчёт RMSE для всех данных прошло успешно! "
                        f"Затрачено времени: {timer_end - timer_start}")
            return result
        except Exception as error:
            error_message: str = "Произошла ошибка при расчёте RMSE"
            raise http_error(error_message, error, logger=logger)
