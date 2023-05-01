import pandas as pd


class TimeSeriesDF:
    def __init__(self, data):
        self.df_work: pd.DataFrame = data
        self.main_parameter: list | None = None
        self.data_params: list = list(self.df_work.columns)
