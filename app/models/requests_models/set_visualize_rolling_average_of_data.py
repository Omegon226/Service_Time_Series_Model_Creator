from pydantic import BaseModel


class SetVisualizeRollingAverageOfData(BaseModel):
    fig_weights: float = 15.
    fig_height: float = 5.
    window_size: int = 5
