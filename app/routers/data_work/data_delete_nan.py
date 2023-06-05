from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_data_delete_nan import SetDataDeleteNan
from app.models.requests_models.set_data_change_nan import SetDataChangeNan
from app.scripts.data_work.data_delete_nan import DeleterOfNanValues
from app.models.data_models.time_series_df import TimeSeriesDF


router_data_delete_nan = APIRouter(prefix="/data_delete_nan")
router_data_delete_nan_test = APIRouter(prefix="/test_data_delete_nan")


@router_data_delete_nan.post("/delete_nan/")
async def delete_nan():
    result = DeleterOfNanValues.delete_nan_values(app.service_global_variables.data.time_series_work)

    app.service_global_variables.data.time_series_work = result
    return {"columns": result.df_work.columns.tolist(),
            "values": result.df_work.values.tolist(),
            "nan_count": str(result.df_work.isna().sum().sum())}


@router_data_delete_nan.post("/change_nan/")
async def change_nan(request: SetDataChangeNan):
    result = DeleterOfNanValues.change_nan_values(app.service_global_variables.data.time_series_work,
                                                  type_of_editing=request.type_of_editing,
                                                  window_size=request.window_size)

    app.service_global_variables.data.time_series_work = result
    return {"columns": result.df_work.columns.tolist(),
            "values": result.df_work.values.tolist(),
            "nan_count": str(result.df_work.isna().sum().sum())}


@router_data_delete_nan_test.get("/test_check_time_series_work_df/")
async def test_check_time_series_work_df():
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict(),
            "result_influencing_param": app.service_global_variables.data.time_series_work.main_parameter,
            "nan count": str(app.service_global_variables.data.time_series_work.df_work.isna().sum().sum())}
