import requests
import pandas as pd

HOST = "127.0.0.1"
PORT = 8000


class RequestsDataWork:
    @staticmethod
    def request_get_all_params():
        return requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_all_params_of_time_series/").json()[
            "all_params"]

    @staticmethod
    def request_get_df():
        return pd.DataFrame(requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_all_data_frame/").json())

    @staticmethod
    def request_get_all_params_statistics():
        params = RequestsDataWork.request_get_all_params()
        params = {"params_statistics": params}
        return pd.DataFrame.from_dict(requests.post(f"http://{HOST}:{PORT}/data_manipulation/get_statistics_of_time_series/",
                                      json=params).json()["statistics"])
