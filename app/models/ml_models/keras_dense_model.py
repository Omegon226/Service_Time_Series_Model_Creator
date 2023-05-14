from app.models.data_models.time_series_df import TimeSeriesDF
from app.scripts.http_error import http_error
from app.models.ml_models.ml_model_base import MLModelBase
import keras
import keras.layers
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.lib.stride_tricks import sliding_window_view
import numpy as np
import dill
import os
import io

sns.set_theme()


class KerasDenseModel(MLModelBase):
    def __init__(self, hidden_layers_size: list, hidden_layers_activation: list, amount_of_params: int,
                 horizon_for_prediction: int, horizon_of_prediction: int, param_for_prediction: str,
                 loss="huber", optimizer="adam", metrics="MSE", name="KerasDenseModel", **kwargs):

        input_layer = keras.Input(shape=(horizon_for_prediction, amount_of_params), name="input_layer")
        flatten_layer = keras.layers.Flatten(name="flatten_layer")(input_layer)
        hidden_layers = []
        for iteration in range(len(hidden_layers_size)):
            if iteration == 0:
                try:
                    hidden_layers += [keras.layers.Dense(hidden_layers_size[iteration],
                                                         activation=hidden_layers_activation[iteration],
                                                         name=f"hidden_{iteration + 1}_dense")(flatten_layer)]
                except (ValueError, IndexError) as error:
                    hidden_layers += [keras.layers.Dense(hidden_layers_size[iteration],
                                                         activation="relu",
                                                         name=f"hidden_{iteration + 1}_dense")(flatten_layer)]
            else:
                try:
                    hidden_layers += [keras.layers.Dense(hidden_layers_size[iteration],
                                                         activation=hidden_layers_activation[iteration],
                                                         name=f"hidden_{iteration + 1}_dense")(hidden_layers[-1])]
                except (ValueError, IndexError) as error:
                    hidden_layers += [keras.layers.Dense(hidden_layers_size[iteration],
                                                         activation="relu",
                                                         name=f"hidden_{iteration + 1}_dense")(hidden_layers[-1])]
        output_layer = keras.layers.Dense(horizon_of_prediction, name="output_layer")(hidden_layers[-1])

        self.keras_model = keras.Model(inputs=input_layer, outputs=output_layer, name=name)
        self.keras_model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
        self.horizon_for_prediction = horizon_for_prediction
        self.horizon_of_prediction = horizon_of_prediction
        self.amount_of_params = amount_of_params
        self.param_for_prediction = param_for_prediction
        self.name = name

        if "epochs" in kwargs.keys():
            self.epochs = kwargs["epochs"]
        else:
            self.epochs = 5
        if "validation_split" in kwargs.keys():
            self.validation_split = kwargs["validation_split"]
        else:
            self.validation_split = 0.2
        if "test_split" in kwargs.keys():
            self.test_split = kwargs["test_split"]
        else:
            self.test_split = 0.2

    def fit(self, data, epochs=None, validation_split=None, test_split=None, return_plot=True, **kwargs):
        if epochs is None:
            epochs = self.epochs
        if validation_split is None:
            validation_split = self.validation_split
        if test_split is None:
            test_split = self.test_split

        columns = list(data.columns)

        x = sliding_window_view(data.values[:-self.horizon_of_prediction],
                                window_shape=(self.horizon_for_prediction, data.shape[1]))
        x = np.squeeze(x)
        y = sliding_window_view(data.values[self.horizon_for_prediction:],
                                window_shape=(self.horizon_of_prediction, data.shape[1]))
        y = np.squeeze(y)[:, :, columns.index(self.param_for_prediction)]

        test_size = int(x.shape[0] * test_split)

        train_x = x[:-test_size]
        train_y = y[:-test_size]
        test_x = x[-test_size:]
        test_y = y[-test_size:]

        self.keras_model.fit(x=train_x, y=train_y, epochs=epochs, validation_split=validation_split)

        if "tests" in kwargs.keys():
            tests_results = {}
            result = self.keras_model.predict(test_x)
            result_sq = np.squeeze(result)
            test_y_sq = np.squeeze(test_y)
            for test in kwargs["tests"]:
                tests_results[test.get_metric_name()] = test.calculate_metric(result_sq, test_y_sq)

            if return_plot:
                return self.__create_plot_of_accuracy(data), tests_results

        else:
            if return_plot:
                return self.__create_plot_of_accuracy(data)

    def __create_plot_of_accuracy(self, data):
        x = sliding_window_view(data.values[:-self.horizon_of_prediction],
                                window_shape=(self.horizon_for_prediction, data.shape[1]))
        x = np.squeeze(x)
        x = x[-1].reshape(1, x.shape[1], x.shape[2])

        columns = list(data.columns)

        result = self.keras_model.predict(x)
        x_1 = np.arange(0, data.shape[0])
        x_2 = np.arange(data.shape[0], data.shape[0] + self.horizon_of_prediction)

        plt.rcParams['figure.figsize'] = [7, 6]
        plt.rcParams['figure.autolayout'] = True
        fig = plt.figure()
        plt.plot(x_1, data.values[:, columns.index(self.param_for_prediction)])
        plt.plot(x_2, result.reshape(-1))
        img_buf = io.BytesIO()
        plt.savefig(img_buf, format='png')
        plt.close(fig)
        return img_buf

    def predict(self, data):
        x = sliding_window_view(data[:-self.horizon_of_prediction],
                                window_shape=(self.horizon_for_prediction, data.shape[1]))
        x = np.squeeze(x)
        x = x[-1].reshape(1, x.shape[1], x.shape[2])

        return self.keras_model.predict(x)

    def save(self, path: str = "app/resources/testing_ml_models", name: str = "keras_dense_model"):
        self.keras_model.save(os.path.join(path, name+".keras"), save_format="keras")
        del self.keras_model
        with open(os.path.join(path, name+".dill"), 'wb+') as file:
            dill.dump(self, file)

    @staticmethod
    def load(path: str = "app/resources/testing_ml_models", name: str = "keras_dense_model"):
        with open(os.path.join(path, name+".dill"), 'rb+') as file:
            keras_dense_model = dill.load(file)
        keras_dense_model.keras_model = keras.models.load_model(os.path.join(path, name+".keras"))
        return keras_dense_model
