from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_influencing_param import SetDataInfluencingParamRequest
from app.scripts.data_work.data_change_influencing_param import SetterOfInfluencingParameter
from app.models.data_models.time_series_df import TimeSeriesDF


router_data_change_influencing_param = APIRouter(prefix="/data_change_influencing_param")


@router_data_change_influencing_param.post("/set_param/")
async def set_param(request: SetDataInfluencingParamRequest):
    result = SetterOfInfluencingParameter.set_influencing_parameter(app.service_global_variables.data.time_series_work,
                                                                    parameter_to_set_influencing=request.parameter_to_set_influencing)

    app.service_global_variables.data.time_series_work = result
    return {"result": "Запрос был выполнен успешно!"}


@router_data_change_influencing_param.get("/test_check_time_series_work_df/")
async def test_check_time_series_work_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_influencing_param": app.service_global_variables.data.time_series_work.main_parameter}