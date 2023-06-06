from pydantic import BaseModel


class SetMLModelToFindCreationParameters(BaseModel):
    ml_model: str = "keras_dense"
