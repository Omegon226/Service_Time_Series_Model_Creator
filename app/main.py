from fastapi import FastAPI

import logging
from time import perf_counter

# Подключение routers
from routers.data_work.data_importer import router_data_import


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
        - Подключение routers
    """
    app.include_router(router_data_import)


if __name__ == "__main__":
    # При запуске через отладчик PyCharm (и др. IDE) или через консоль файла main,py
    main()
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
else:
    # При запуске через команду Uvicorn
    main()












