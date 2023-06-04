from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
from app.models.requests_models.set_visualize_rolling_average_of_data import SetVisualizeRollingAverageOfData
from app.scripts.visualization.visualize_rolling_average_of_data import VisualiserRollingAverageOfData
from app.models.data_models.time_series_df import TimeSeriesDF


router_visualise_rolling_average_of_data = APIRouter(prefix="/visualize_rolling_average_of_data")
router_visualise_rolling_average_of_data_test = APIRouter(prefix="/test_visualize_rolling_average_of_data")


@router_visualise_rolling_average_of_data.post("/create_rolling_average_of_selected_data/")
async def create_rolling_average_of_selected_data(background_tasks: BackgroundTasks,
                                                  request: SetVisualizeRollingAverageOfData):
    img = VisualiserRollingAverageOfData.create_rolling_average_main_param_img(
        app.service_global_variables.data.time_series_work,
        window_size=request.window_size,
        fig_weights=request.fig_weights,
        fig_height=request.fig_height)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_visualise_rolling_average_of_data_test.get("/test_rolling_average/")
async def test_rolling_average(background_tasks: BackgroundTasks):
    img = VisualiserRollingAverageOfData.create_rolling_average_test_img(window_size=5)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')
