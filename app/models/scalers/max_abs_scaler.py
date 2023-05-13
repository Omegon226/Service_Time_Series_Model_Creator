from app.models.scalers.scaler_base import ScalerBase
from sklearn.preprocessing import MaxAbsScaler as SklearnMaxAbsScaler
import dill
import os


class MaxAbsScaler(ScalerBase):
    def __init__(self):
        self.scikit_learn_scaler = SklearnMaxAbsScaler()

    def fit(self, data):
        self.scikit_learn_scaler.fit(data)

    def transform(self, data):
        return self.scikit_learn_scaler.transform(data)

    def save(self, path: str = "app/resources/testing_scalers", name: str = "max_abs_scaler"):
        with open(os.path.join(path, name+".dill"), 'wb+') as file:
            dill.dump(self, file)

    @staticmethod
    def load(path: str = "app/resources/testing_scalers", name: str = "max_abs_scaler"):
        with open(os.path.join(path, name+".dill"), 'rb+') as file:
            return dill.load(file)

    def get_feature_names_out(self):
        return self.scikit_learn_scaler.get_feature_names_out()
