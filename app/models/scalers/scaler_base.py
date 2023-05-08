from abc import ABC, abstractmethod


class ScalerBase(ABC):

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def transform(self, data):
        pass

    @abstractmethod
    def get_feature_names_out(self):
        pass
