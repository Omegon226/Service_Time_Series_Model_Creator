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
file_handler = logging.FileHandler("app/logs/scripts.visualise_violinplot_of_data.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class VisualiserViolinplotOfData:
    @staticmethod
    def create_violinplot_test_img():
        logger.info(f"Происходит создание тестовой визуализации (violinplot)")
        try:
            timer_start: float = perf_counter()

            plt.rcParams['figure.figsize'] = [15, 5]
            plt.rcParams['figure.autolayout'] = True
            fig = plt.figure()
            sns.violinplot(data=[1, 2, 3, 6, 9, 12])
            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            plt.close(fig)

            timer_end: float = perf_counter()
            logger.info(f"Создание тестовой визуализации (violinplot) прошло успешно!"
                        f"Затрачено времени: {timer_end - timer_start}")

            return img_buf
        except Exception as error:
            error_message: str = f"Входе создании тестовой (violinplot) визуализации произошла ошибка"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def create_violinplot_img(time_series_df: TimeSeriesDF, fig_weights: float = 15., fig_height: float = 5.,
                              params: list | None = None):
        logger.info(f"Происходит создание визуализации всех временных рядов (violinplot)")
        try:
            timer_start: float = perf_counter()

            plt.rcParams['figure.figsize'] = [fig_weights, fig_height]
            plt.rcParams['figure.autolayout'] = True
            fig = plt.figure()
            if params is None:
                sns.violinplot(data=time_series_df.df_work)
            else:
                sns.violinplot(data=time_series_df.df_work[params])
            plt.title("Визуализация временных рядов")
            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            plt.close(fig)

            timer_end: float = perf_counter()
            logger.info(f"Создание визуализации (violinplot) прошло успешно!"
                        f"Затрачено времени: {timer_end - timer_start}")

            return img_buf
        except Exception as error:
            error_message: str = f"Входе создании визуализации (violinplot) произошла ошибка"
            http_error(error_message, error, logger=logger)
