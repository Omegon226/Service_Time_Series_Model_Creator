from pydantic import BaseModel
from typing import Union, List, Dict


class SetPipelineCreationData(BaseModel):
    scalers: List[str] = ["min_max_scaler", "max_abs_scaler"]
    ml_models: Dict[str, Dict] = {"keras_dense_1": {"model": "keras_dense",
                                                    "hidden_layers_size": [100, 200],
                                                    "hidden_layers_activation": ["relu", "relu"],
                                                    "amount_of_params": 5,
                                                    "horizon_for_prediction": 100,
                                                    "horizon_of_prediction": 10},
                                  "keras_dense_2": {"model": "keras_dense",
                                                    "hidden_layers_size": [100],
                                                    "hidden_layers_activation": ["relu"],
                                                    "amount_of_params": 5,
                                                    "horizon_for_prediction": 100,
                                                    "horizon_of_prediction": 10},
                                  "keras_rnn": {"model": "keras_rnn",
                                                    "hidden_layers_size": [20, 20],
                                                    "hidden_layers_activation": ["relu", "relu"],
                                                    "amount_of_params": 5,
                                                    "horizon_for_prediction": 100,
                                                    "horizon_of_prediction": 10},
                                  "keras_gru": {"model": "keras_gru",
                                                    "hidden_layers_size": [20, 20],
                                                    "hidden_layers_activation": ["relu", "relu"],
                                                    "amount_of_params": 5,
                                                    "horizon_for_prediction": 100,
                                                    "horizon_of_prediction": 10},
                                  "keras_lstm": {"model": "keras_lstm",
                                                    "hidden_layers_size": [20, 20],
                                                    "hidden_layers_activation": ["relu", "relu"],
                                                    "amount_of_params": 5,
                                                    "horizon_for_prediction": 100,
                                                    "horizon_of_prediction": 10}}
    tests: List[str] = ["mse", "rmse", "r2", "mae"]
