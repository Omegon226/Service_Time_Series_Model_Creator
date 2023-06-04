from pydantic import BaseModel

from app.models.requests_models.set_visualization_base import SetVisualizeBase


class SetVisualizeRollingStatisticsOfData(SetVisualizeBase):
    window_size: int = 5
