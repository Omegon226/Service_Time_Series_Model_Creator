from app.models.scalers.max_abs_scaler import MaxAbsScaler
from app.models.scalers.min_max_scaler import MinMaxScaler
from app.models.scalers.standard_scaler import StandardScaler

from app.models.ml_models.keras_dense_model import KerasDenseModel
from app.models.ml_models.keras_rnn_model import KerasRNNModel
from app.models.ml_models.keras_gru_model import KerasGRUModel
from app.models.ml_models.keras_lstm_model import KerasLSTMModel

from app.models.tests.mse_test import MSETest
from app.models.tests.rmse_test import RMSETest
from app.models.tests.r2_test import R2Test
from app.models.tests.mae_test import MAETest


# Здесь будут находиться все комбинации пайплайнов

pipelines: list = []

# Здесь хранятся все доступные для использования скейлеры, модели и методы тестирования

all_scalers = {"max_abs_scaler": MaxAbsScaler, "min_max_scaler": MinMaxScaler, "standard_scaler": StandardScaler}
all_ml_models = {"keras_dense": KerasDenseModel, "keras_rnn": KerasRNNModel, "keras_gru": KerasGRUModel,
                 "keras_lstm": KerasLSTMModel}
all_tests = {"mse": MSETest, "rmse": RMSETest, "r2": R2Test, "mae": MAETest}
