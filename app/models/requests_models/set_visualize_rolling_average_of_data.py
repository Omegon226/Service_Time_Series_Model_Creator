from pydantic import BaseModel


class SetVisualizeRollingAverageOfData(BaseModel):
    window_size: int = 5
