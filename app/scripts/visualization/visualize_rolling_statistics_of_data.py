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
file_handler = logging.FileHandler("app/logs/scripts.visualize_rolling_statistics_of_data.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class VisualiserRollingStatisticsOfData:
    @staticmethod
    def create_rolling_statistics_test_img(window_size: int):
        logger.info(f"Происходит создание тестовой визуализации (rolling_statistics)")
        try:
            timer_start: float = perf_counter()

            plt.rcParams['figure.figsize'] = [15, 10]
            plt.rcParams['figure.autolayout'] = True
            fig, ax = plt.subplots(2, 1, dpi=200)
            data = pd.DataFrame({"data": (np.arange(1, 100)) ** 1.2})

            rolling_mean = data.rolling(window=window_size).mean()
            #rolling_mean = rolling_mean.fillna(rolling_mean.mean())
            rolling_median = data.rolling(window=window_size).median()
            #rolling_median = rolling_median.fillna(value=rolling_median.mean())
            rolling_std = data.rolling(window=window_size).std()
            #rolling_std = rolling_std.fillna(value=rolling_std.mean())
            rolling_min = data.rolling(window=window_size).min()
            #rolling_min = rolling_min.fillna(value=rolling_min.mean())
            rolling_max = data.rolling(window=window_size).max()
            #rolling_max = rolling_max.fillna(value=rolling_max.mean())
            rolling_range = rolling_max - rolling_min
            #rolling_range = rolling_range.fillna(value=rolling_range.mean())

            ax[0].plot(rolling_mean, label="Движущееся среднее арифметическое")
            ax[0].plot(rolling_median, label="Движущаяся медиана")
            ax[0].plot(rolling_min, label="Движущееся минимальное значение")
            ax[0].plot(rolling_max, label="Движущееся максимальное значение")
            ax[1].plot(rolling_std, label="Движущееся стандартное отклонение")
            ax[1].plot(rolling_range, label="Движущейся размах")

            ax[0].legend()
            ax[1].legend()

            ax[0].set_title("Движущиеся среднее арифм., медиана, минимум и максимум")
            ax[1].set_title("Движущиеся размах, стандартное отклонение")

            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            plt.close(fig)

            timer_end: float = perf_counter()
            logger.info(f"Создание тестовой визуализации (rolling_statistics) прошло успешно!"
                        f"Затрачено времени: {timer_end - timer_start}")

            return img_buf
        except Exception as error:
            error_message: str = f"Входе создании тестовой (rolling_statistics) визуализации произошла ошибка"
            http_error(error_message, error, logger=logger)

    @staticmethod
    def create_rolling_statistics_img(time_series_df: TimeSeriesDF, window_size: int, fig_weights: float = 15.,
                                      fig_height: float = 10.,  params: list | None = None):
        logger.info(f"Происходит создание визуализации статистики параметра {params} (rolling_statistics)")
        try:
            timer_start: float = perf_counter()

            if time_series_df.main_parameter is None:
                error_message = "Для создания визуализации движущегося среднего (rolling_statistics) нужно знать главный параметр"
                raise Exception(error_message)

            plt.rcParams['figure.figsize'] = [fig_weights, fig_height]
            plt.rcParams['figure.autolayout'] = True
            fig, ax = plt.subplots(2, 1, dpi=200)

            rolling_mean = time_series_df.df_work[params].rolling(window=window_size).mean()
            #rolling_mean = rolling_mean.fillna(rolling_mean.mean())
            rolling_median = time_series_df.df_work[params].rolling(window=window_size).median()
            #rolling_median = rolling_median.fillna(value=rolling_median.mean())
            rolling_std = time_series_df.df_work[params].rolling(window=window_size).std()
            #rolling_std = rolling_std.fillna(value=rolling_std.mean())
            rolling_min = time_series_df.df_work[params].rolling(window=window_size).min()
            #rolling_min = rolling_min.fillna(value=rolling_min.mean())
            rolling_max = time_series_df.df_work[params].rolling(window=window_size).max()
            #rolling_max = rolling_max.fillna(value=rolling_max.mean())
            rolling_range = rolling_max - rolling_min
            #rolling_range = rolling_range.fillna(value=rolling_range.mean())

            ax[0].plot(rolling_mean, label="Движущееся среднее арифметическое")
            ax[0].plot(rolling_median, label="Движущаяся медиана")
            ax[0].plot(rolling_min, label="Движущееся минимальное значение")
            ax[0].plot(rolling_max, label="Движущееся максимальное значение")
            ax[1].plot(rolling_std, label="Движущееся стандартное отклонение")
            ax[1].plot(rolling_range, label="Движущейся размах")

            ax[0].legend()
            ax[1].legend()

            ax[0].set_title(f"Движущиеся среднее арифм., медиана, минимум и максимум параметра/ов: {params}")
            ax[1].set_title(f"Движущиеся размах, стандартное отклонение параметра/ов: {params}")

            img_buf = io.BytesIO()
            plt.savefig(img_buf, format='png')
            plt.close(fig)

            timer_end: float = perf_counter()
            logger.info(f"Создание визуализации (rolling_statistics) прошло успешно!"
                        f"Затрачено времени: {timer_end - timer_start}")

            return img_buf
        except Exception as error:
            error_message: str = f"Входе создании визуализации (rolling_statistics) для параметра/ов {params} произошла ошибка"
            http_error(error_message, error, logger=logger)
