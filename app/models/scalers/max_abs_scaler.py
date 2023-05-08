from app.models.scalers.scaler_base import ScalerBase
from sklearn.preprocessing import MaxAbsScaler as SklearnMaxAbsScaler


class MaxAbsScaler(ScalerBase):
    def __init__(self):
        self.scikit_learn_scaler = SklearnMaxAbsScaler()

    def fit(self, data):
        self.scikit_learn_scaler.fit(data)

    def transform(self, data):
        return self.scikit_learn_scaler.transform(data)

    def get_feature_names_out(self):
        return self.scikit_learn_scaler.get_feature_names_out()
