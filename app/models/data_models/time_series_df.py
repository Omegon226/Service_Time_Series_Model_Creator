import pandas as pd


class TimeSeriesDF:
    def __init__(self, data):
        self.df_work: pd.DataFrame = data
        self.influencing_parameter: list | None = None
