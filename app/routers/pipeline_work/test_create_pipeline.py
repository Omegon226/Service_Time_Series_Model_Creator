from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
#from app.models.requests_models.set_data_main_param import SetDataMainParamRequest
from app.scripts.pipeline_work.test_create_pipeline import TesterCreatePipeline
from app.models.data_models.time_series_df import TimeSeriesDF


router_test_create_pipeline_test = APIRouter(prefix="/test_create_pipeline")


@router_test_create_pipeline_test.get("/test_create_pipeline/")
async def test_create_dense_model():
    pipeline = TesterCreatePipeline.create_pipeline(app.service_global_variables.data.time_series_work)
    return {"result_pipeline": str(pipeline.__dict__)}


@router_test_create_pipeline_test.get("/test_create_and_fit_pipeline/")
async def test_create_and_fit_pipeline(background_tasks: BackgroundTasks):
    img = TesterCreatePipeline.create_and_fit_pipeline(app.service_global_variables.data.time_series_work)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_test_create_pipeline_test.get("/test_create_fit_and_predict_pipeline/")
async def test_create_fit_and_predict_pipeline():
    prediction = TesterCreatePipeline.create_fit_and_predict_pipeline(app.service_global_variables.data.time_series_work)
    return {"result_of_prediction": prediction.tolist()}


@router_test_create_pipeline_test.get("/test_save_pipeline/")
async def test_save_pipeline():
    TesterCreatePipeline.save_pipeline(app.service_global_variables.data.time_series_work)
    return {"result_save": "check save"}


@router_test_create_pipeline_test.get("/test_load_pipeline/")
async def test_load_pipeline():
    pipeline = TesterCreatePipeline.load_pipeline()
    return {"result_pipeline": str(pipeline.__dict__)}
