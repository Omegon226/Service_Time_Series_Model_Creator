from pydantic import BaseModel
from typing import Union, List, Dict


class SetPipelineCreationData(BaseModel):
    scalers: List[str] = ["min_max_scaler", "max_abs_scaler"]
    ml_models: Dict[str, list] = {"keras_dense_1": ["keras_dense", [100, 200], ["relu", "relu"], 5, 100, 10],
                                  "keras_dense_2": ["keras_dense", [100], ["relu"], 5, 100, 10]}
    tests: List[str] = ["mse", "rmse"]
