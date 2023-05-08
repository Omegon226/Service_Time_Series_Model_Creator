from fastapi import APIRouter

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.scalers_work.create_scalers import CreatorCreateScalers
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_scalers = APIRouter(prefix="/test_scalers")


@router_test_scalers.get("/test_create_max_abs_scaler/")
async def test_check_time_series_work_df():
    scaler = CreatorCreateScalers.create_max_abs_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}


@router_test_scalers.get("/test_create_min_max_scaler/")
async def test_check_time_series_work_df():
    scaler = CreatorCreateScalers.create_min_mas_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}


@router_test_scalers.get("/test_create_standard_scaler/")
async def test_check_time_series_work_df():
    scaler = CreatorCreateScalers.create_standard_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}
