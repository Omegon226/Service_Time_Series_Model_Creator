from fastapi import APIRouter

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.scalers_work.test_scalers import TesterCreateScalers
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_scalers_test = APIRouter(prefix="/test_scalers")


@router_test_scalers_test.get("/test_create_max_abs_scaler/")
async def test_create_max_abs_scaler():
    scaler = TesterCreateScalers.create_max_abs_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}


@router_test_scalers_test.get("/test_create_min_max_scaler/")
async def test_create_min_max_scaler():
    scaler = TesterCreateScalers.create_min_max_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}


@router_test_scalers_test.get("/test_create_standard_scaler/")
async def test_create_standard_scaler():
    scaler = TesterCreateScalers.create_standard_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}


@router_test_scalers_test.get("/test_create_standard_scaler/")
async def test_create_standard_scaler():
    scaler = TesterCreateScalers.create_standard_scaler_for_all_data(app.service_global_variables.data.time_series_work)

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}


@router_test_scalers_test.get("/test_save_min_max_scaler/")
async def test_save_min_max_scaler():
    TesterCreateScalers.save_min_max_scaler(TesterCreateScalers.create_min_max_scaler_for_all_data(
        app.service_global_variables.data.time_series_work))

    return {"result": "check save"}


@router_test_scalers_test.get("/test_load_min_max_scaler/")
async def test_load_min_max_scaler():
    scaler = TesterCreateScalers.load_min_max_scaler()

    return {"result_scaler": str(scaler.scikit_learn_scaler.__dict__)}
