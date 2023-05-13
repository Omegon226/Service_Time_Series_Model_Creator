from fastapi import APIRouter

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.scalers_work.test_column_transformer import TesterColumnTransformer
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_column_transformer_test = APIRouter(prefix="/test_column_transformer")


@router_test_column_transformer_test.get("/test_creation_column_transformer/")
async def test_creation_column_transformer():
    column_transformer = TesterColumnTransformer.create_column_transformer(
        app.service_global_variables.data.time_series_work)
    return {"result_column_transformer": str(column_transformer.__dict__),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict()}


@router_test_column_transformer_test.get("/test_check_creation_of_new_columns_by_column_transformer/")
async def test_check_creation_of_new_columns_by_column_transformer():
    TesterColumnTransformer.create_column_transformer_with_creating_new_columns(
        app.service_global_variables.data.time_series_work)
    return {"result_type": str(type(app.service_global_variables.data.time_series_work)),
            "result_data": app.service_global_variables.data.time_series_work.df_work.head(4).to_dict()}


@router_test_column_transformer_test.get("/test_save_column_transformer/")
async def test_save_column_transformer():
    TesterColumnTransformer.save_column_transformer(TesterColumnTransformer.create_column_transformer(
        app.service_global_variables.data.time_series_work))

    return {"result": "check save"}


@router_test_column_transformer_test.get("/test_load_column_transformer/")
async def test_load_column_transformer():
    column_transformer = TesterColumnTransformer.load_column_transformer()

    return {"result_column_transformer ": str(column_transformer.__dict__)}


@router_test_column_transformer_test.get("/test_check_needed_data/")
async def test_check_needed_data():
    result = TesterColumnTransformer.check_needed_data(app.service_global_variables.data.time_series_work)

    return {"result": result}


@router_test_column_transformer_test.get("/test_sort_columns_in_needed_sequence/")
async def test_sort_columns_in_needed_sequence():
    result = TesterColumnTransformer.sort_columns_in_needed_sequence(app.service_global_variables.data.time_series_work)

    return {"result": result.head(4).to_dict()}
