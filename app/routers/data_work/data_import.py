from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_from_csv import SetDataFromCSVRequest
from app.models.requests_models.set_data_from_dict import SetDataFromDictRequest
from app.models.requests_models.set_data_from_json import SetDataFromJSONRequest
from app.scripts.data_work.data_import import Importer
from app.models.data_models.time_series_df import TimeSeriesDF

router_data_import = APIRouter(prefix="/data_import")


@router_data_import.post("/set_data_from_csv/")
async def set_data_from_csv(request: SetDataFromCSVRequest):
    result = Importer.import_data_from_csv(full_path=request.full_path,
                                           sep=request.sep,
                                           decimal=request.decimal,
                                           encoding=request.encoding)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"result": "Запрос был выполнен успешно!"}


@router_data_import.post("/set_data_from_dict/")
async def set_data_from_dict(request: SetDataFromDictRequest):
    result = Importer.import_data_from_dict(data=request.data)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"result": "Запрос был выполнен успешно!"}


@router_data_import.post("/set_data_from_json/")
async def set_data_from_json(request: SetDataFromJSONRequest):
    result = Importer.import_data_from_json(full_path=request.full_path,
                                            encoding=request.encoding)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"result": "Запрос был выполнен успешно!"}


@router_data_import.get("/test_check_time_series_worf_df/")
async def test_check_time_series_worf_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_influencing_param": app.service_global_variables.data.time_series_work.influencing_parameter}
