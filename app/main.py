from fastapi import FastAPI

import logging
from time import perf_counter

# Импорт routers
from routers.data_work.data_import import router_data_import
from routers.data_work.data_change_influencing_param import router_data_change_influencing_param
from routers.data_work.data_delete_nan import router_data_delete_nan
from routers.data_work.data_manipulation import router_data_manipulation
from routers.data_work.data_create_param import router_data_create_param

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
    app.include_router(router_data_change_influencing_param)
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

    logger.info("Все роутеры были успешно подключены!")


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












