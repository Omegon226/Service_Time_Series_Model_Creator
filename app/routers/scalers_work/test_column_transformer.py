from fastapi import APIRouter

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.scalers_work.create_column_transformer import CreatorColumnTransformer
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_column_transformer = APIRouter(prefix="/test_column_transformer")


@router_test_column_transformer.get("/test_creation_column_transformer/")
async def test_check_creation_of_new_columns_by_column_transformer():
    column_transformer = CreatorColumnTransformer.create_column_transformer(
        app.service_global_variables.data.time_series_work)
    return {"column_transformer": str(column_transformer.__dict__),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict()}


@router_test_column_transformer.get("/test_check_creation_of_new_columns_by_column_transformer/")
async def test_check_creation_of_new_columns_by_column_transformer():
    CreatorColumnTransformer.create_column_transformer_with_creating_new_columns(
        app.service_global_variables.data.time_series_work)
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict()}
