import dill
import numpy as np
import pandas as pd
import os

from app.models.ml_models.keras_dense_model import KerasDenseModel
from app.models.scalers.column_transformer import ColumnTransformer
from app.models.scalers.min_max_scaler import MinMaxScaler


class Pipeline:
    def __init__(self, column_transformer, scaler, ml_model):
        self.column_transformer = column_transformer
        self.scaler = scaler
        self.ml_model = ml_model

    def fit(self, data, **kwargs):
        data = self.__check_and_transform_data(data)

        self.scaler.fit(data)
        data_scaled = self.scaler.transform(data)
        data_scaled = pd.DataFrame(data_scaled, columns=data.columns)

        if "tests" in kwargs.keys():
            plot, tests = self.ml_model.fit(data_scaled, return_plot=True, **kwargs)
            return plot, tests
        else:
            plot = self.ml_model.fit(data_scaled, return_plot=True, **kwargs)
            return plot

    def predict(self, data):
        data = self.__check_and_transform_data(data)

        columns = data.columns
        data_scaled = self.scaler.transform(data)

        prediction = self.ml_model.predict(data_scaled)

        param_for_prediction = self.ml_model.param_for_prediction
        data_for_inverse_transform = np.random.rand(prediction.shape[1], columns.shape[0])
        data_for_inverse_transform = pd.DataFrame(data_for_inverse_transform, columns=columns)
        data_for_inverse_transform[param_for_prediction] = prediction.reshape(-1)
        result = self.scaler.inverse_transform(data_for_inverse_transform)[:,
                                                                           columns.tolist().index(param_for_prediction)]

        return result

    def __check_and_transform_data(self, data):
        if not self.column_transformer.check_for_needed_columns(data):
            data = self.column_transformer.create_new_columns(data)
        data = self.column_transformer.sort_columns_in_needed_sequence(data)
        return data

    def save(self, path: str = "app/resources/testing_pipelines", name: str = "pipeline"):
        os.mkdir(os.path.join(path, name))
        self.column_transformer.save(path=os.path.join(path, name))
        self.scaler.save(path=os.path.join(path, name))
        self.ml_model.save(path=os.path.join(path, name))

    @staticmethod
    def load(path: str = "app/resources/testing_pipelines", name: str = "pipeline"):
        column_transformer = ColumnTransformer.load(os.path.join(path, name))
        scaler = MinMaxScaler.load(os.path.join(path, name))
        ml_model = KerasDenseModel.load(os.path.join(path, name))

        return Pipeline(column_transformer, scaler, ml_model)
