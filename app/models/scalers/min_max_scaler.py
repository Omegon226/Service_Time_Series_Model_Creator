from app.models.scalers.scaler_base import ScalerBase
from sklearn.preprocessing import MinMaxScaler as SklearnMinMaxScaler
import joblib
import os


class MinMaxScaler(ScalerBase):
    def __init__(self):
        self.scikit_learn_scaler = SklearnMinMaxScaler()

    def fit(self, data):
        self.scikit_learn_scaler.fit(data)

    def transform(self, data):
        return self.scikit_learn_scaler.transform(data)

    def save(self, path: str = "app/resources/testing_scalers", name: str = "min_max_scaler"):
        joblib.dump(self, os.path.join(path, name+".joblib"))

    @staticmethod
    def load(path: str = "app/resources/testing_scalers", name: str = "min_max_scaler.joblib"):
        return joblib.load(os.path.join(path, name))

    def get_feature_names_out(self):
        return self.scikit_learn_scaler.get_feature_names_out()
