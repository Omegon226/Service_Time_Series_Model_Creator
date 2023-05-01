from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import logging
from time import perf_counter

# Импорт routers
from routers.data_work.data_import import router_data_import
from routers.data_work.data_change_main_param import router_data_change_main_param
from routers.data_work.data_delete_nan import router_data_delete_nan
from routers.data_work.data_manipulation import router_data_manipulation
from routers.data_work.data_create_param import router_data_create_param
from routers.visualization.visualise_plot_of_data import router_visualise_plot_of_data
from routers.visualization.visualise_violinplot_of_data import router_visualise_violinplot_of_data
from routers.visualization.visualise_hist_of_data import router_visualise_hist_of_data
from routers.visualization.visualise_boxplot_of_data import router_visualise_boxplot_of_data
from routers.visualization.visualise_corrheatmap_of_data import router_visualise_corrheatmap_of_data
from routers.visualization.visualize_rolling_statistics_of_data import router_visualise_rolling_statistics_of_data
from routers.visualization.visualize_rolling_average_of_data import router_visualise_rolling_average_of_data

# Создание приложения FastAPI
app = FastAPI()

# Создание логгера для main.py
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/main.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


def main():
    """
    В этой функции выполняются основные функции при запуске приложения
    Что здесь происходит:
        - Подключение router
    """
    logger.info("Идёт подключение роутера для импорта данных в сервис")
    app.include_router(router_data_import)
    logger.info("Роутер для импорта данных в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для изменения влияющего параметра")
    app.include_router(router_data_change_main_param)
    logger.info("Роутер для изменения влияющего параметра в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для работы с NaN значениями")
    app.include_router(router_data_delete_nan)
    logger.info("Роутер для работы с NaN значениями в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для манипуляции над данными")
    app.include_router(router_data_manipulation)
    logger.info("Роутер для манипуляции над данными в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания нового параметра")
    app.include_router(router_data_create_param)
    logger.info("Роутер для создания нового параметра в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (plot)")
    app.include_router(router_visualise_plot_of_data)
    logger.info("Роутер для создания визуализации временных рядов (plot) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (violinplot)")
    app.include_router(router_visualise_violinplot_of_data)
    logger.info("Роутер для создания визуализации временных рядов (violinplot) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (hist)")
    app.include_router(router_visualise_hist_of_data)
    logger.info("Роутер для создания визуализации временных рядов (hist) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (boxplot)")
    app.include_router(router_visualise_boxplot_of_data)
    logger.info("Роутер для создания визуализации временных рядов (boxplot) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (corrheatmap)")
    app.include_router(router_visualise_corrheatmap_of_data)
    logger.info("Роутер для создания визуализации временных рядов (corrheatmap) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (rolling_statistics)")
    app.include_router(router_visualise_rolling_statistics_of_data)
    logger.info("Роутер для создания визуализации временных рядов (rolling_statistics) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для создания визуализации временных рядов (rolling_average)")
    app.include_router(router_visualise_rolling_average_of_data)
    logger.info("Роутер для создания визуализации временных рядов (rolling_average) в сервис успешно подключён!")

    logger.info("Все роутеры были успешно подключены!")


@app.get("/")
def redirect_to_swagger_docs():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    # При запуске через отладчик PyCharm (и др. IDE) или через консоль файла main.py
    logger.info("Произведён запуск сервиса через отладчик или через обращение к файлу main.py")
    main()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    # При запуске через команду Uvicorn (пример: python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000)
    logger.info("Произведён запуск сервиса через команду python -m uvicorn")
    main()












