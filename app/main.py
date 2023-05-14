from fastapi import FastAPI
from fastapi.responses import RedirectResponse

import logging
from time import perf_counter

# Импорт routers
from routers.data_work.data_import import router_data_import, router_data_import_test
from routers.data_work.data_change_main_param import router_data_change_main_param, router_data_change_main_param_test
from routers.data_work.data_delete_nan import router_data_delete_nan, router_data_delete_nan_test
from routers.data_work.data_manipulation import router_data_manipulation, router_data_manipulation_test
from routers.data_work.data_create_param import router_data_create_param, router_data_create_param_test
from routers.visualization.visualise_plot_of_data import router_visualise_plot_of_data, router_visualise_plot_of_data_test
from routers.visualization.visualise_violinplot_of_data import router_visualise_violinplot_of_data, router_visualise_violinplot_of_data_test
from routers.visualization.visualise_hist_of_data import router_visualise_hist_of_data, router_visualise_hist_of_data_test
from routers.visualization.visualise_boxplot_of_data import router_visualise_boxplot_of_data, router_visualise_boxplot_of_data_test
from routers.visualization.visualise_corrheatmap_of_data import router_visualise_corrheatmap_of_data, router_visualise_corrheatmap_of_data_test
from routers.visualization.visualize_rolling_statistics_of_data import router_visualise_rolling_statistics_of_data, router_visualise_rolling_statistics_of_data_test
from routers.visualization.visualize_rolling_average_of_data import router_visualise_rolling_average_of_data, router_visualise_rolling_average_of_data_test
from routers.scalers_work.test_scalers import router_test_scalers_test
from routers.scalers_work.test_column_transformer import router_test_column_transformer_test
from routers.ml_models_work.test_ml_models import router_test_ml_models_test
from routers.pipeline_work.test_create_pipeline import router_test_create_pipeline_test
from routers.tests_work.test_tests import router_test_tests_test


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
    logger.info("Идёт подключение роутеров для импорта данных в сервис")
    app.include_router(router_data_import)
    app.include_router(router_data_import_test)
    logger.info("Роутеры для импорта данных в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для изменения влияющего параметра")
    app.include_router(router_data_change_main_param)
    app.include_router(router_data_change_main_param_test)
    logger.info("Роутеры для изменения влияющего параметра в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для работы с NaN значениями")
    app.include_router(router_data_delete_nan)
    app.include_router(router_data_delete_nan_test)
    logger.info("Роутеры для работы с NaN значениями в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для манипуляции над данными")
    app.include_router(router_data_manipulation)
    app.include_router(router_data_manipulation_test)
    logger.info("Роутеры для манипуляции над данными в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания нового параметра")
    app.include_router(router_data_create_param)
    app.include_router(router_data_create_param_test)
    logger.info("Роутеры для создания нового параметра в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (plot)")
    app.include_router(router_visualise_plot_of_data)
    app.include_router(router_visualise_plot_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (plot) в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (violinplot)")
    app.include_router(router_visualise_violinplot_of_data)
    app.include_router(router_visualise_violinplot_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (violinplot) в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (hist)")
    app.include_router(router_visualise_hist_of_data)
    app.include_router(router_visualise_hist_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (hist) в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (boxplot)")
    app.include_router(router_visualise_boxplot_of_data)
    app.include_router(router_visualise_boxplot_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (boxplot) в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (corrheatmap)")
    app.include_router(router_visualise_corrheatmap_of_data)
    app.include_router(router_visualise_corrheatmap_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (corrheatmap) в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (rolling_statistics)")
    app.include_router(router_visualise_rolling_statistics_of_data)
    app.include_router(router_visualise_rolling_statistics_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (rolling_statistics) в сервис успешно подключён!")

    logger.info("Идёт подключение роутеров для создания визуализации временных рядов (rolling_average)")
    app.include_router(router_visualise_rolling_average_of_data)
    app.include_router(router_visualise_rolling_average_of_data_test)
    logger.info("Роутеры для создания визуализации временных рядов (rolling_average) в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для тестирования создания скейлеров")
    app.include_router(router_test_scalers_test)
    logger.info("Роутер для тестирования скейлеров в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для тестирования создания колумн трансформера")
    app.include_router(router_test_column_transformer_test)
    logger.info("Роутер для тестирования колумн трансформера в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для тестирования ML Моделей")
    app.include_router(router_test_ml_models_test)
    logger.info("Роутер для тестирования ML Моделей в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для тестирования Пайплайнов")
    app.include_router(router_test_create_pipeline_test)
    logger.info("Роутер для тестирования Пайплайнов в сервис успешно подключён!")

    logger.info("Идёт подключение роутера для тестирования Тестов")
    app.include_router(router_test_tests_test)
    logger.info("Роутер для тестирования Тестов в сервис успешно подключён!")

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












