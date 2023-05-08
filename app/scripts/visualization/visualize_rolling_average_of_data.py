import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

import logging
from time import perf_counter
import io

from app.scripts.http_error import http_error
from app.models.data_models.time_series_df import TimeSeriesDF

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.visualize_rolling_average_of_data.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class VisualiserRollingAverageOfData:
    @staticmethod
    def create_rolling_average_test_img(window_size: int):
        logger.info(f"Происходит создание тестовой визуализации (rolling_average)")
        try:
            timer_start: float = perf_counter()

            plt.rcParams['figure.figsize'] = [15, 5]
            plt.rcParams['figure.autolayout'] = True
            fig = plt.figure()
            data = pd.DataFrame({"data": (np.arange(1, 100)) ** 1.2})

            rolling_mean = data.rolling(window=window_size).mean()
            rolling_median = data.rolling(window=window_size).median()
            rolling_std = data.rolling(window=window_size).std()
            upper_bond = rolling_mean + 1.96 * rolling_std
            lower_bond = rolling_mean - 1.96 * rolling_std

            plt.title("Движущееся среднее\n размер окна = {}".format(window_size))
            plt.plot(rolling_mean, "g", label="Движущееся среднее арифметическое")
            plt.plot(rolling_median, label="Движущаяся медиана")

            plt.plot(upper_bond, "r--", label="Верхняя граница / Нижняя граница")
            plt.plot(lower_bond, "r--")
            plt.plot(data, "purple", label="Действительные значения")
            plt.legend()
            plt.grid(True)

            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            plt.close(fig)

            timer_end: float = perf_counter()
            logger.info(f"Создание тестовой визуализации (rolling_average) прошло успешно!"
                        f"Затрачено времени: {timer_end - timer_start}")

            return img_buf
        except Exception as error:
            error_message: str = f"Входе создании тестовой (rolling_average) визуализации произошла ошибка"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def create_rolling_average_main_param_img(time_series_df: TimeSeriesDF, window_size: int):
        logger.info(f"Происходит создание визуализации движущегося среднего (rolling_average) для основного параметра")
        try:
            timer_start: float = perf_counter()

            if time_series_df.main_parameter is None:
                error_message = "Для создания визуализации движущегося среднего (rolling_average) нужно знать главный параметр"
                raise Exception(error_message)

            plt.rcParams['figure.figsize'] = [15, 5]
            plt.rcParams['figure.autolayout'] = True
            fig = plt.figure()

            rolling_mean = time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).mean()
            rolling_median = time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).median()
            rolling_std = time_series_df.df_work[time_series_df.main_parameter].rolling(window=window_size).std()
            upper_bond = rolling_mean + 1.96 * rolling_std
            lower_bond = rolling_mean - 1.96 * rolling_std

            plt.title("Движущееся среднее\n размер окна = {}".format(window_size))
            plt.plot(rolling_mean, "g", label="Движущееся среднее арифметическое")
            plt.plot(rolling_median, label="Движущаяся медиана")

            plt.plot(upper_bond, "r--", label="Верхняя граница / Нижняя граница")
            plt.plot(lower_bond, "r--")
            plt.plot(time_series_df.df_work[time_series_df.main_parameter], "purple", label="Действительные значения")
            plt.legend()
            plt.grid(True)

            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            plt.close(fig)

            timer_end: float = perf_counter()
            logger.info(f"Создание визуализации (rolling_average) прошло успешно!"
                        f"Затрачено времени: {timer_end - timer_start}")

            return img_buf
        except Exception as error:
            error_message: str = f"Входе создании визуализации (rolling_average) для основного параметра произошла ошибка"
            http_error(error_message, error, logger=logger)
