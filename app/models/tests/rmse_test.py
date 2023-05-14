from sklearn.metrics import mean_squared_error
import numpy as np

from app.models.tests.test_base import TestBase


class RMSETest(TestBase):
    @staticmethod
    def calculate_metric(predicted: np.array, true: np.array):
        return float(mean_squared_error(true, predicted, squared=False))

    @staticmethod
    def get_metric_name():
        return "rmse"
