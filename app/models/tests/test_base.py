from abc import ABC, abstractmethod
import numpy as np


class TestBase(ABC):

    @staticmethod
    @abstractmethod
    def calculate_metric(predicted: np.array, true: np.array):
        pass

    @staticmethod
    @abstractmethod
    def get_metric_name():
        pass
