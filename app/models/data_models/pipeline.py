import dill
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

    def fit(self, data):
        data = self.__check_and_transform_data(data)

        columns = data.columns
        self.scaler.fit(data)
        data = self.scaler.transform(data)
        data = pd.DataFrame(data, columns=columns)

        plot = self.ml_model.fit(data, return_plot=True)

        return plot

    def predict(self, data):
        data = self.__check_and_transform_data(data)

        columns = data.columns
        data = self.scaler.transform(data)

        result = self.ml_model.predict(data)

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
