from fastapi import APIRouter, UploadFile, Depends, File, Form

import app.service_global_variables.data
from app.models.requests_models.set_data_from_csv import SetDataFromCSVRequest
from app.models.requests_models.set_data_from_dict import SetDataFromDictRequest
from app.models.requests_models.set_data_from_json import SetDataFromJSONRequest
from app.models.requests_models.set_data_from_csv_file import SetDataFromCSVFileRequest
from app.models.requests_models.set_data_from_json_file import SetDataFromJSONFileRequest
from app.scripts.data_work.data_import import Importer
from app.models.data_models.time_series_df import TimeSeriesDF

router_data_import = APIRouter(prefix="/data_import")
router_data_import_test = APIRouter(prefix="/test_data_import")


@router_data_import.post("/set_data_from_csv/")
async def set_data_from_csv(request: SetDataFromCSVRequest):
    result = Importer.import_data_from_csv(full_path=request.full_path,
                                           sep=request.sep,
                                           decimal=request.decimal,
                                           encoding=request.encoding)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"columns": app.service_global_variables.data.time_series_work.df_work.columns.tolist(),
            "values": result.values.tolist()}


@router_data_import.post("/set_data_from_dict/")
async def set_data_from_dict(request: SetDataFromDictRequest):
    result = Importer.import_data_from_dict(data=request.data)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"columns": app.service_global_variables.data.time_series_work.df_work.columns.tolist(),
            "values": result.values.tolist()}


@router_data_import.post("/set_data_from_json/")
async def set_data_from_json(request: SetDataFromJSONRequest):
    result = Importer.import_data_from_json(full_path=request.full_path,
                                            encoding=request.encoding)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"columns": app.service_global_variables.data.time_series_work.df_work.columns.tolist(),
            "values": result.values.tolist()}


@router_data_import.post("/set_data_from_csv_file/")
async def set_data_from_csv_file(request: SetDataFromCSVFileRequest = Depends(),
                                 file: UploadFile = File(...)):
    result = Importer.import_data_from_uploaded_csv_file(file=file.file,
                                                         sep=request.sep,
                                                         decimal=request.decimal,
                                                         encoding=request.encoding)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"columns": app.service_global_variables.data.time_series_work.df_work.columns.tolist(),
            "values": result.values.tolist()}


@router_data_import.post("/set_data_from_json_file/")
async def set_data_from_json_file(request: SetDataFromJSONFileRequest = Depends(),
                                  file: UploadFile = File(...)):
    result = Importer.import_data_from_uploaded_json_file(file=file.file,
                                                          encoding=request.encoding)
    app.service_global_variables.data.time_series_work = TimeSeriesDF(result)
    return {"columns": app.service_global_variables.data.time_series_work.df_work.columns.tolist(),
            "values": result.values.tolist()}


@router_data_import_test.get("/test_check_time_series_work_df/")
async def test_check_time_series_work_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_influencing_param": app.service_global_variables.data.time_series_work.main_parameter}
