from app.models.scalers.max_abs_scaler import MaxAbsScaler
from app.models.scalers.min_max_scaler import MinMaxScaler
from app.models.scalers.standart_scaler import StandardScaler

from app.models.ml_models.keras_dense_model import KerasDenseModel

from app.models.tests.mse_test import MSETest
from app.models.tests.rmse_test import RMSETest


# Здесь будут находиться все комбинации пайплайнов

pipelines: list = []

# Здесь хранятся все доступные для использования скейлеры, модели и методы тестирования

all_scalers = {"max_abs_scaler": MaxAbsScaler, "min_max_scaler": MinMaxScaler, "standard_scaler": StandardScaler}
all_models = {"keras_dense": KerasDenseModel}
all_test = {"mse": MSETest, "rmse": RMSETest}
