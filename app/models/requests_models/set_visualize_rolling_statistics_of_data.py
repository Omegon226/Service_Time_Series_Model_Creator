from pydantic import BaseModel


class SetVisualizeRollingStatisticsOfData(BaseModel):
    window_size: int = 5
    params_for_analyze: str | list = "07HAH10CP901"
