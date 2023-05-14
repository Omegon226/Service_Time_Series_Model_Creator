from sklearn.metrics import mean_squared_error
import numpy as np

from app.models.tests.test_base import TestBase


class RMSETest(TestBase):
    @staticmethod
    def calculate_metric(predicted: np.array, true: np.array):
        return mean_squared_error(true, predicted, squared=False)
