from fastapi import APIRouter

from app.models.requests_models.set_ml_model_to_find_creation_variables import SetMLModelToFindCreationParameters
from app.scripts.pipeline_work.information_for_creation import InformationForCreation


router_information_for_creation = APIRouter(prefix="/information_for_creation")
router_information_for_creation_test = APIRouter(prefix="/test_information_for_creation")


@router_information_for_creation.get("/get_all_scalers/")
async def get_all_scalers():
    result = InformationForCreation.get_all_scalers()
    return {"scalers": result}


@router_information_for_creation.get("/get_all_ml_model/")
async def get_all_model():
    result = InformationForCreation.get_all_ml_model()
    return {"ml_models": result}


@router_information_for_creation.get("/get_all_tests/")
async def get_all_tests():
    result = InformationForCreation.get_all_tests()
    return {"tests": result}


@router_information_for_creation.post("/get_all_variables_for_model_creation/")
async def get_all_parameters_for_model_creation(request: SetMLModelToFindCreationParameters):
    result = InformationForCreation.get_all_parameters_for_model_creation(request.ml_model)
    return {"ml_model": request.ml_model,
            "parameters": result}
