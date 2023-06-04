from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.ml_models_work.test_ml_models import TesterMlModels
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_ml_models_test = APIRouter(prefix="/test_ml_models")


@router_test_ml_models_test.get("/test_create_dense_model/")
async def test_create_dense_model():
    model = TesterMlModels.create_dense_model()
    return {"result_model": str(model.keras_model)}


@router_test_ml_models_test.get("/test_fit_dense_model/")
async def test_fit_dense_model():
    TesterMlModels.fit_dense_model(app.service_global_variables.data.time_series_work)
    return {"result_of_fit": "all worked well"}


@router_test_ml_models_test.get("/test_fit_dense_model_and_get_plot/")
async def test_fit_dense_model_and_get_plot(background_tasks: BackgroundTasks):
    img = TesterMlModels.fit_dense_model_and_get_plot(app.service_global_variables.data.time_series_work)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_test_ml_models_test.get("/test_predict_dense_model/")
async def test_predict_dense_model():
    result = TesterMlModels.predict_dense_model(app.service_global_variables.data.time_series_work)
    return {"result_of_predict": result.tolist()}


@router_test_ml_models_test.get("/test_save_dense_model/")
async def test_save_dense_model():
    TesterMlModels.save_dense_model()
    return {"result_save": "check save"}


@router_test_ml_models_test.get("/test_load_dense_model/")
async def test_load_dense_model():
    model = TesterMlModels.load_dense_model()
    return {"result_loaded_model": str(model.keras_model)}


@router_test_ml_models_test.get("/test_get_params_for_construction_dense_model/")
async def test_get_params_for_construction_dense_model():
    params = TesterMlModels.get_params_for_construction_dense_model()
    return {"result_loaded_model": params}