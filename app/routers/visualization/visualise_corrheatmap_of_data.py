from fastapi import APIRouter, BackgroundTasks, Response

import app.service_global_variables.data
from app.models.requests_models.set_visualization_base import SetVisualizeBase
from app.scripts.visualization.visualise_corrheatmap_of_data import VisualiserCorrheatmapOfData
from app.models.data_models.time_series_df import TimeSeriesDF


router_visualise_corrheatmap_of_data = APIRouter(prefix="/visualise_corrheatmap_of_data")
router_visualise_corrheatmap_of_data_test = APIRouter(prefix="/test_visualise_corrheatmap_of_data")


@router_visualise_corrheatmap_of_data.post("/create_corrheatmap_spearman_of_all_data/")
async def create_corrheatmap_spearman_of_all_data(background_tasks: BackgroundTasks,
                                                  request: SetVisualizeBase):
    img = VisualiserCorrheatmapOfData.create_corrheatmap_spearman_img(
        app.service_global_variables.data.time_series_work,
        fig_weights=request.fig_weights,
        fig_height=request.fig_height,
        params=request.params)

    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_visualise_corrheatmap_of_data.post("/create_corrheatmap_pearson_of_all_data/")
async def create_corrheatmap_pearson_of_all_data(background_tasks: BackgroundTasks,
                                                  request: SetVisualizeBase):
    img = VisualiserCorrheatmapOfData.create_corrheatmap_pearson_img(
        app.service_global_variables.data.time_series_work,
        fig_weights=request.fig_weights,
        fig_height=request.fig_height,
        params=request.params)
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')


@router_visualise_corrheatmap_of_data_test.get("/test_corrheatmap/")
async def test_corrheatmap(background_tasks: BackgroundTasks):
    img = VisualiserCorrheatmapOfData.create_corrheatmap_test_img()
    background_tasks.add_task(img.close)
    headers = {'Content-Disposition': 'inline; filename="out.png"'}
    return Response(img.getvalue(), headers=headers, media_type='image/png')
