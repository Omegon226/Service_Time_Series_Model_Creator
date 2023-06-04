from sklearn.metrics import mean_absolute_error
import numpy as np

from app.models.tests.test_base import TestBase


class MAETest(TestBase):
    @staticmethod
    def calculate_metric(predicted: np.array, true: np.array):
        return float(mean_absolute_error(true, predicted))

    @staticmethod
    def get_metric_name():
        return "mae"
