from io import BytesIO
import json

import requests
import pandas as pd
from streamlit.runtime.uploaded_file_manager import UploadedFile

HOST = "127.0.0.1"
PORT = 8000


class RequestsDataImport:
    @staticmethod
    def request_get_all_params():
        return requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_all_params_of_time_series/").json()["all_params"]

    @staticmethod
    def request_get_df():
        return pd.DataFrame(requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_all_data_frame/").json())

    @staticmethod
    def request_set_data_from_csv(file: UploadedFile):
        requests.post(f"http://{HOST}:{PORT}/data_import/set_data_from_csv_file/",
                      files={'file': file.getbuffer()})

    @staticmethod
    def request_set_data_from_json(file: UploadedFile):
        requests.post(f"http://{HOST}:{PORT}/data_import/set_data_from_json_file/",
                      files={'file': file.getbuffer()})

    @staticmethod
    def request_set_data_from_dict(dict_like_text):
        requests.post(f"http://{HOST}:{PORT}/data_import/set_data_from_dict/",
                      json={"data": json.loads(dict_like_text)})
