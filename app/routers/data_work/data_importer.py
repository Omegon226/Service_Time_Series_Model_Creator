from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_from_csv import SetDataFromCSVRequest
from app.models.requests_models.set_data_from_dict import SetDataFromDictRequest
from app.models.requests_models.set_data_from_json import SetDataFromJSONRequest
from app.scripts.data_work.data_importer import Importer

router_data_import = APIRouter(prefix="/data_import")


@router_data_import.post("/set_data_from_csv/")
def set_data_from_csv_(request: SetDataFromCSVRequest):
    app.service_global_variables.data.time_series_worf_df = Importer.import_data_from_csv(full_path=request.full_path,
                                                                                          sep=request.sep,
                                                                                          decimal=request.decimal,
                                                                                          encoding=request.encoding)

    return {"result": "Запрос был выполнен успешно!"}


@router_data_import.post("/set_data_from_dict/")
def set_data_from_dict_(request: SetDataFromDictRequest):
    app.service_global_variables.data.time_series_worf_df = Importer.import_data_from_dict(data=request.data)

    return {"result": "Запрос был выполнен успешно!"}


@router_data_import.post("/set_data_from_json/")
def set_data_from_json_(request: SetDataFromJSONRequest):
    app.service_global_variables.data.time_series_worf_df = Importer.import_data_from_json(full_path=request.full_path,
                                                                                           encoding=request.encoding)

    return {"result": "Запрос был выполнен успешно!"}


@router_data_import.get("/test_check_time_series_worf_df/")
def test_check_time_series_worf_df():
    return {"result": str(type(app.service_global_variables.data.time_series_worf_df))}
