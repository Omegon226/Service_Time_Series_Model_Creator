from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_drop_columns import SetDataDropColumns
from app.models.requests_models.set_data_statistics_of_df import SetDataStatisticsOfDf
from app.models.requests_models.set_data_change_data_params import SetDataChangeDataParams
from app.scripts.data_work.data_manipulation import DataManipulator
from app.models.data_models.time_series_df import TimeSeriesDF


router_data_manipulation = APIRouter(prefix="/data_manipulation")


@router_data_manipulation.post("/get_statistics_of_time_series/")
async def get_statistics_of_time_series(request: SetDataStatisticsOfDf):
    result = DataManipulator.get_statistics_of_time_series(app.service_global_variables.data.time_series_work)
    return {"result": "Запрос был выполнен успешно!",
            "statistics": str(result)}


@router_data_manipulation.post("/drop_columns/")
async def drop_columns(request: SetDataDropColumns):
    result = DataManipulator.drop_columns(app.service_global_variables.data.time_series_work,
                                          columns_to_drop=request.columns_to_drop)

    app.service_global_variables.data.time_series_work = result
    return {"result": "Запрос был выполнен успешно!"}


@router_data_manipulation.post("/change_data_params/")
async def change_data_params(request: SetDataChangeDataParams):
    result = DataManipulator.change_data_params(app.service_global_variables.data.time_series_work,
                                                new_data_params=request.new_data_params)

    app.service_global_variables.data.time_series_work = result
    return {"result": "Запрос был выполнен успешно!"}


@router_data_manipulation.get("/test_check_time_series_work_df/")
async def test_check_time_series_work_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_influencing_param": app.service_global_variables.data.time_series_work.main_parameter,
            "result_data_params": app.service_global_variables.data.time_series_work.data_params,
            "result_sequence_of_creating_new_params": app.service_global_variables.data.time_series_work.sequence_of_creating_new_params}
