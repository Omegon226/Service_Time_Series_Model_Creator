from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_drop_columns import SetDataDropColumns
from app.models.requests_models.set_data_statistics_of_df import SetDataStatisticsOfDf
from app.models.requests_models.set_data_change_data_params import SetDataChangeDataParams
from app.scripts.data_work.data_manipulation import DataManipulator
from app.models.data_models.time_series_df import TimeSeriesDF


router_data_manipulation = APIRouter(prefix="/data_manipulation")
router_data_manipulation_test = APIRouter(prefix="/test_data_manipulation")


@router_data_manipulation.get("/get_all_params_of_time_series/")
async def get_all_params_of_time_series():
    params = DataManipulator.get_all_params(app.service_global_variables.data.time_series_work)
    return {"all_params": params}


@router_data_manipulation.get("/get_main_param_of_time_series/")
async def get_all_params_of_time_series():
    params = DataManipulator.get_all_params(app.service_global_variables.data.time_series_work)
    return {"all_params": params}


@router_data_manipulation.get("/get_data_params_of_time_series/")
async def get_all_params_of_time_series():
    params = DataManipulator.get_all_params(app.service_global_variables.data.time_series_work)
    return {"all_params": params}


@router_data_manipulation.get("/get_all_data_frame/")
async def get_all_data_frame():
    data: dict = DataManipulator.get_full_data_frame(app.service_global_variables.data.time_series_work)
    return data


@router_data_manipulation.post("/get_statistics_of_time_series/")
async def get_statistics_of_time_series(request: SetDataStatisticsOfDf):
    result = DataManipulator.get_statistics_of_time_series(app.service_global_variables.data.time_series_work,
                                                           params_statistics=request.params_statistics)
    return {"statistics": result}


@router_data_manipulation.post("/drop_columns/")
async def drop_columns(request: SetDataDropColumns):
    result = DataManipulator.drop_columns(app.service_global_variables.data.time_series_work,
                                          columns_to_drop=request.columns_to_drop)

    app.service_global_variables.data.time_series_work = result
    return {"dropped_columns": request.columns_to_drop,
            "columns": app.service_global_variables.data.time_series_work.df_work.columns.tolist(),
            "values": result.df_work.values.tolist()}


@router_data_manipulation.post("/change_data_params/")
async def change_data_params(request: SetDataChangeDataParams):
    result = DataManipulator.change_data_params(app.service_global_variables.data.time_series_work,
                                                new_data_params=request.new_data_params)

    app.service_global_variables.data.time_series_work = result
    return {"new_data_params": request.new_data_params}


@router_data_manipulation_test.get("/test_check_time_series_work_df/")
async def test_check_time_series_work_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_influencing_param": app.service_global_variables.data.time_series_work.main_parameter,
            "result_data_params": app.service_global_variables.data.time_series_work.data_params,
            "result_sequence_of_creating_new_params": app.service_global_variables.data.time_series_work.sequence_of_creating_new_params}
