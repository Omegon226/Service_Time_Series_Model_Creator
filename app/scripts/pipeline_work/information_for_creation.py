import logging
from time import perf_counter
import io

from app.scripts.http_error import http_error
import app.service_global_variables.pipelines

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(10)
logg_formatter = logging.Formatter(fmt=f"%(asctime)s|%(levelname)s|{logger.name}|%(message)s")
# Добавляем ротируемый вывод логгера в файл
file_handler = logging.FileHandler("app/logs/scripts.information_for_creation.log.txt", mode="a+")
file_handler.setFormatter(logg_formatter)
logger.addHandler(file_handler)
# Добавляем вывод логгера в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(logg_formatter)
logger.addHandler(console_handler)


class InformationForCreation:
    @staticmethod
    def get_all_scalers():
        return list(app.service_global_variables.pipelines.all_scalers.keys())

    @staticmethod
    def get_all_ml_models():
        return list(app.service_global_variables.pipelines.all_ml_models.keys())

    @staticmethod
    def get_all_tests():
        return list(app.service_global_variables.pipelines.all_scalers.keys())

    @staticmethod
    def get_all_parameters_for_model_creation(ml_model: str):
        try:
            parameters = app.service_global_variables.pipelines.all_ml_models[ml_model].get_params_for_construction()
            if type(parameters) in [dict, list]:
                return parameters
            else:
                return list(parameters)
        except Exception as error:
            error_message: str = f"Произошла ошибка при получении параметров для создания модели"
            http_error(error_message, error, logger=logger)
