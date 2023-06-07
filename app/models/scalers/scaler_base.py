from abc import ABC, abstractmethod


class ScalerBase(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def inverse_transform(self, data):
        pass

    @abstractmethod
    def save(self, path: str, name: str):
        pass

    @staticmethod
    @abstractmethod
    def load(path: str, name: str):
        pass

    @abstractmethod
    def get_feature_names_out(self):
        pass
