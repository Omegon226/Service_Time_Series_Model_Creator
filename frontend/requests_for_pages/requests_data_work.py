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

    @staticmethod
    def request_set_main_param(param):
        json_data = {"parameter_to_set_main": param}

        requests.post(f"http://{HOST}:{PORT}/data_change_main_param/set_param/", json=json_data)
        return requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_main_param_of_time_series/").json()["main_param"]

    @staticmethod
    def request_change_data_params(params):
        json_data = {"new_data_params": params}

        requests.post(f"http://{HOST}:{PORT}/data_manipulation/change_data_params/", json=json_data)
        return requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_data_params_of_time_series/").json()["data_params"]

    @staticmethod
    def request_create_new_param(type_of_new_param):
        json_data = {"type_of_param": "", "name_of_new_param": "", "window_size": 5}

        match type_of_new_param:
            case "Mean":
                json_data["type_of_param"] = "mean"
                json_data["name_of_new_param"] = "mean"
            case "Median":
                json_data["type_of_param"] = "median"
                json_data["name_of_new_param"] = "median"
            case "Range":
                json_data["type_of_param"] = "range"
                json_data["name_of_new_param"] = "range"
            case "STD":
                json_data["type_of_param"] = "std"
                json_data["name_of_new_param"] = "std"

        result = requests.post(f"http://{HOST}:{PORT}/data_create_param/create_new_param/",
                               json=json_data).json()

        return pd.DataFrame({result["name_of_new_param"]: result["data_of_new_param"]})

    @staticmethod
    def request_change_nan(type_of_changing_nan):
        json_data = {"type_of_editing": "zero", "window_size": 5}

        if type_of_changing_nan == "Drop Rows":
            return requests.post(f"http://{HOST}:{PORT}/data_delete_nan/delete_nan/").json()["nan_count"]
        else:
            match type_of_changing_nan:
                case "Zero":
                    json_data["type_of_editing"] = "zero"
                case "Mean":
                    json_data["type_of_editing"] = "mean"
                case "Median":
                    json_data["type_of_editing"] = "median"

            return requests.post(f"http://{HOST}:{PORT}/data_delete_nan/change_nan/",
                                 json=json_data).json()["nan_count"]

