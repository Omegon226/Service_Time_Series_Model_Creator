from fastapi import APIRouter

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.tests_work.test_tests import TesterTests
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_tests_test = APIRouter(prefix="/test_tests_test")


@router_test_tests_test.get("/test_mse/")
async def test_mse():
    metric = TesterTests.test_mse()

    return {"result_metric": metric}


@router_test_tests_test.get("/test_rmse/")
async def test_rmse():
    metric = TesterTests.test_rmse()

    return {"result_metric": metric}
