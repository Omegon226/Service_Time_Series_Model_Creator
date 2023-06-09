from fastapi import APIRouter

import app.service_global_variables.data
from app.models.requests_models.set_pipeline_creation_data import SetPipelineCreationData
from app.scripts.pipeline_work.pipelines_creator import PipelineCreator
from app.models.data_models.time_series_df import TimeSeriesDF


router_pipelines_creator = APIRouter(prefix="/pipelines_creator")
router_pipelines_creator_test = APIRouter(prefix="/test_pipelines_creator")


@router_pipelines_creator.post("/create_pipelines/")
async def test_create_pipelines(request: SetPipelineCreationData):
    PipelineCreator.create_pipelines(request, app.service_global_variables.data.time_series_work)
    return {"result": "Запрос был выполнен успешно!"}


@router_pipelines_creator.post("/get_best_pipelines/")
async def get_best_pipelines(amount: int = 2, nom_of_pipeline_creation: int = 1):
    result = PipelineCreator.get_best_pipelines(amount, nom_of_pipeline_creation)
    return {"best_pipelines_by_metric": result}


@router_pipelines_creator.get("/get_amount_of_ml_pipelines_dirs/")
async def get_amount_of_ml_pipelines_dirs():
    result = PipelineCreator.get_amount_of_ml_pipelines_dirs()
    return {"amount_of_dirs": result}


@router_pipelines_creator_test.post("/test_request/")
async def test_request(request: SetPipelineCreationData):
    return {"result_scalers": request.scalers,
            "result_ml_models": request.ml_models,
            "result_tests": request.tests}


