from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
from app.models.requests_models.set_visualize_rolling_statistics_of_data import SetVisualizeRollingStatisticsOfData
from app.scripts.visualization.visualize_rolling_statistics_of_data import VisualiserRollingStatisticsOfData
from app.models.data_models.time_series_df import TimeSeriesDF


router_visualise_rolling_statistics_of_data = APIRouter(prefix="/visualize_rolling_statistics_of_data")
router_visualise_rolling_statistics_of_data_test = APIRouter(prefix="/test_visualize_rolling_statistics_of_data")


@router_visualise_rolling_statistics_of_data.post("/create_rolling_statistics_of_selected_data/")
async def create_rolling_statistics_of_selected_data(background_tasks: BackgroundTasks,
                                                     request: SetVisualizeRollingStatisticsOfData):
    img = VisualiserRollingStatisticsOfData.create_rolling_statistics_img(
        app.service_global_variables.data.time_series_work,
        window_size=request.window_size,
        fig_weights=request.fig_weights,
        fig_height=request.fig_height,
        params=request.params)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_visualise_rolling_statistics_of_data_test.get("/test_rolling_statistics/")
async def test_rolling_statistics(background_tasks: BackgroundTasks):
    img = VisualiserRollingStatisticsOfData.create_rolling_statistics_test_img(window_size=5)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')
