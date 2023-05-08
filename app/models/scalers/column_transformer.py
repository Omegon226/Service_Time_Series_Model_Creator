from app.models.data_models.time_series_df import TimeSeriesDF
from app.scripts.http_error import http_error


class ColumnTransformer:
    def __init__(self, data: TimeSeriesDF):
        self.sequence_of_creating_new_params = data.sequence_of_creating_new_params

    def create_new_columns(self, time_series_df: TimeSeriesDF):
        try:
            for new_param in self.sequence_of_creating_new_params:

                if new_param["param"] == "mean":
                    time_series_df = ColumnTransformer._add_mean(time_series_df, new_param["param_name"],
                                                                 new_param["data_params"])
                elif new_param["param"] == "median":
                    time_series_df = ColumnTransformer._add_median(time_series_df, new_param["param_name"],
                                                                   new_param["data_params"])
                elif new_param["param"] == "range":
                    time_series_df = ColumnTransformer._add_range(time_series_df, new_param["param_name"],
                                                                  new_param["data_params"])
                elif new_param["param"] == "std":
                    time_series_df = ColumnTransformer._add_std(time_series_df, new_param["param_name"],
                                                                new_param["data_params"])
                elif new_param["param"] == "rolling mean":
                    time_series_df = ColumnTransformer._add_rolling_mean(time_series_df, new_param["param_name"],
                                                                         new_param["data_params"],
                                                                         new_param["window_size"])
                elif new_param["param"] == "rolling median":
                    time_series_df = ColumnTransformer._add_rolling_median(time_series_df, new_param["param_name"],
                                                                           new_param["data_params"],
                                                                           new_param["window_size"])
                elif new_param["param"] == "rolling range":
                    time_series_df = ColumnTransformer._add_rolling_range(time_series_df, new_param["param_name"],
                                                                          new_param["data_params"],
                                                                          new_param["window_size"])
                elif new_param["param"] == "rolling std":
                    time_series_df = ColumnTransformer._add_rolling_std(time_series_df, new_param["param_name"],
                                                                        new_param["data_params"],
                                                                        new_param["window_size"])
                else:
                    error_message = f"Переданный тип параметра ({new_param['param']}) для создания нового параметра " \
                                    f"не существует или не реализован в ColumnTransformer"
                    raise Exception(error_message)

                return time_series_df

        except Exception as error:
            error_message = f"Произошла ошибка при создании новых параметров в объекте ColumnTransformer"
            http_error(error_message, error)

    @staticmethod
    def _add_mean(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "Mean"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].mean(axis=1)

        return time_series_df

    @staticmethod
    def _add_median(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "Median"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].median(axis=1)

        return time_series_df

    @staticmethod
    def _add_range(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "Range"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].max(axis=1) - \
                                                    time_series_df.df_work[data_params].min(axis=1)

        return time_series_df

    @staticmethod
    def _add_std(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = "STD"
        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].std(axis=1)

        return time_series_df

    @staticmethod
    def _add_rolling_mean(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list,
                          window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling Mean {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].rolling(
            window=window_size).mean()

        return time_series_df

    @staticmethod
    def _add_rolling_median(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list,
                            window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling Median {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].rolling(
                window=window_size).median()

        return time_series_df

    @staticmethod
    def _add_rolling_range(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list,
                           window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling Range {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = \
            time_series_df.df_work[data_params].rolling(window=window_size).max() - \
            time_series_df.df_work[data_params].rolling(window=window_size).min()

        return time_series_df

    @staticmethod
    def _add_rolling_std(time_series_df: TimeSeriesDF, name_of_new_param: str | None, data_params: list,
                         window_size: int):
        if name_of_new_param is None or name_of_new_param == "string":
            name_of_new_param = f"Rolling STD {time_series_df.main_parameter}"
        if window_size is None:
            error_message = "Не было указан размер окна для добавления новых данных"
            raise Exception(error_message)
        if time_series_df.main_parameter is None:
            error_message = "Для создания такого параметра нужно знать главный параметр"
            raise Exception(error_message)

        time_series_df.df_work[name_of_new_param] = time_series_df.df_work[data_params].rolling(
                window=window_size).std()

        return time_series_df
