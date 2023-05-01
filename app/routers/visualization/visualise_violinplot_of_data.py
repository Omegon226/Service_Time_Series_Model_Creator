from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
#from app.models.requests_models.set_data_influencing_param import SetDataInfluencingParamRequest
from app.scripts.visualization.visualise_violinplot_of_data import VisualiserViolinplotOfData
from app.models.data_models.time_series_df import TimeSeriesDF


router_visualise_violinplot_of_data = APIRouter(prefix="/visualise_violinplot_of_data")


@router_visualise_violinplot_of_data.post("/create_violinplot_of_all_data/")
async def create_violinplot_of_all_data(background_tasks: BackgroundTasks):
    img = VisualiserViolinplotOfData.create_violinplot_img(app.service_global_variables.data.time_series_work)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_visualise_violinplot_of_data.get("/test_violinplot/")
async def test_violinplot(background_tasks: BackgroundTasks):
    img = VisualiserViolinplotOfData.create_violinplot_test_img()
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')
