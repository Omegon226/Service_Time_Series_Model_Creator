from abc import ABC, abstractmethod


class MLModelBase(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def predict(self, data):
        pass

    @abstractmethod
    def save(self, path: str, name: str):
        pass

    @staticmethod
    @abstractmethod
    def load(path: str, name: str):
        pass

    @staticmethod
    @abstractmethod
    def get_params_for_construction():
        return MLModelBase.__init__.__code__.co_varnames
