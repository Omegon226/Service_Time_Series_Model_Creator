from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
#from app.models.requests_models.set_data_influencing_param import SetDataInfluencingParamRequest
from app.scripts.visualization.visualise_hist_of_data import VisualiserHistOfData
from app.models.data_models.time_series_df import TimeSeriesDF


router_visualise_hist_of_data = APIRouter(prefix="/visualise_hist_of_data")
router_visualise_hist_of_data_test = APIRouter(prefix="/test_visualise_hist_of_data")


@router_visualise_hist_of_data.post("/create_hist_of_all_data/")
async def create_hist_of_all_data(background_tasks: BackgroundTasks):
    img = VisualiserHistOfData.create_hist_img(app.service_global_variables.data.time_series_work)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_visualise_hist_of_data_test.get("/test_hist/")
async def test_hist(background_tasks: BackgroundTasks):
    img = VisualiserHistOfData.create_hist_test_img()
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')
