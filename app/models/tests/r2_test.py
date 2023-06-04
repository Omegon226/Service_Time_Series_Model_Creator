from sklearn.metrics import r2_score
import numpy as np

from app.models.tests.test_base import TestBase


class R2Test(TestBase):
    @staticmethod
    def calculate_metric(predicted: np.array, true: np.array):
        return float(r2_score(true, predicted))

    @staticmethod
    def get_metric_name():
        return "r2"
