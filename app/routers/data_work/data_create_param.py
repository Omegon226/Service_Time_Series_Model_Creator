from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_create_new_param import SetDataCreateNewParam
from app.scripts.data_work.data_create_param import DataCreatorParam
from app.models.data_models.time_series_df import TimeSeriesDF


router_data_create_param = APIRouter(prefix="/data_create_param")
router_data_create_param_test = APIRouter(prefix="/test_data_create_param")


@router_data_create_param.post("/create_new_param/")
async def create_new_param(request: SetDataCreateNewParam):
    result = DataCreatorParam.add_new_column(app.service_global_variables.data.time_series_work,
                                             type_of_param=request.type_of_param,
                                             name_of_new_param=request.name_of_new_param,
                                             window_size=request.window_size)

    app.service_global_variables.data.time_series_work = result.df_work
    return {"name_of_new_param": result.df_work.iloc[:, -1].name,
            "data_of_new_param": result.df_work.iloc[:, -1].values.tolist()}


@router_data_create_param_test.get("/test_check_time_series_work_df/")
async def test_check_time_series_work_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_columns": list(app.service_global_variables.data.time_series_work.df_work.columns)}
