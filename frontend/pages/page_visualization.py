import streamlit as st

from frontend.requests_for_pages.requests_visualization import RequestsVisualization


params_of_df = RequestsVisualization.request_get_all_params()


st.title("Visualization")

tab_timeseries_plot, tab_histogram, tab_boxplot, tab_violinplot, tab_corr_heatmap, tab_rolling_average, \
    tab_rolling_statistics = st.tabs(["Timeseries Plot", "Histogram", "Boxplot", "Violinplot", "Correlation Heatmap",
                                      "Rolling Average", "Rolling Statistics"])


with tab_timeseries_plot:
    width_timeseries_plot = st.slider('Width Timeseries Plot', 1, 20, 8)
    height_timeseries_plot = st.slider('Height Timeseries Plot', 1, 20, 7)
    params_for_timeseries_plot_selected = st.multiselect(
        'Set Parameters to Timeseries Plot',
        params_of_df,
        params_of_df)
    if st.button('Create Timeseries Plot'):
        st.image(RequestsVisualization.request_plot(params_for_timeseries_plot_selected,
                                                    width_timeseries_plot,
                                                    height_timeseries_plot).content)

with tab_histogram:
    width_histogram = st.slider('Width Histogram', 1, 20, 8)
    height_histogram = st.slider('Height Histogram', 1, 20, 7)
    params_for_histogram_selected = st.multiselect(
        'Set Parameters to Histogram',
        params_of_df,
        params_of_df)
    if st.button('Create Histogram'):
        st.image(RequestsVisualization.request_histogram(params_for_histogram_selected,
                                                         width_histogram,
                                                         height_histogram).content)

with tab_boxplot:
    width_boxplot = st.slider('Width Boxplot', 1, 20, 8)
    height_boxplot = st.slider('Height Boxplot', 1, 20, 7)
    params_for_boxplot_selected = st.multiselect(
        'Set Parameters to Boxplot',
        params_of_df,
        params_of_df)
    if st.button('Create Boxplot'):
        st.image(RequestsVisualization.request_boxplot(params_for_boxplot_selected,
                                                       width_boxplot,
                                                       height_boxplot).content)

with tab_violinplot:
    width_violinplot = st.slider('Width Violinplot', 1, 20, 8)
    height_violinplot = st.slider('Height Violinplot', 1, 20, 7)
    params_for_violinplot_selected = st.multiselect(
        'Set Parameters to Violinplot',
        params_of_df,
        params_of_df)
    if st.button('Create Violinplot'):
        st.image(RequestsVisualization.request_violinplot(params_for_violinplot_selected,
                                                          width_violinplot,
                                                          height_violinplot).content)

with tab_corr_heatmap:
    width_corr_heatmap = st.slider('Width Correlation Heatmap', 1, 20, 8)
    height_corr_heatmap = st.slider('Height Correlation Heatmap', 1, 20, 7)
    correlation_option = st.selectbox(
        "Correlation calculation method",
        ("Pearson", "Spearman"))
    params_for_corr_heatmap_selected = st.multiselect(
        'Set Parameters to plot Correlation Heatmap',
        params_of_df,
        params_of_df)
    if st.button('Create Correlation Heatmap'):
        st.image(RequestsVisualization.request_corr_heatmap(correlation_option,
                                                            params_for_corr_heatmap_selected,
                                                            width_corr_heatmap,
                                                            height_corr_heatmap).content)

with tab_rolling_average:
    width_rolling_average = st.slider('Width Rolling Average', 1, 20, 8)
    height_rolling_average = st.slider('Height Rolling Average', 1, 20, 7)
    window_size_rolling_average = st.number_input('Insert window size for Rolling Average',
                                                  step=1, value=15, min_value=1)
    params_for_rolling_statistics_selected = st.multiselect(
        'Set Parameters to plot Rolling Average',
        params_of_df,
        params_of_df)
    if st.button('Create Rolling Average'):
        st.image(RequestsVisualization.request_rolling_average(window_size_rolling_average,
                                                               params_for_rolling_statistics_selected,
                                                               width_rolling_average,
                                                               height_rolling_average).content)

with tab_rolling_statistics:
    width_rolling_statistics = st.slider('Width Rolling Statistics', 1, 20, 8)
    height_rolling_statistics = st.slider('Height Rolling Statistics', 1, 20, 7)
    window_size_rolling_statistics = st.number_input('Insert window size fro Rolling Statistics',
                                                     step=1, value=15, min_value=1)
    if st.button('Create Rolling Statistics'):
        st.image(RequestsVisualization.request_rolling_statistics(window_size_rolling_statistics,
                                                                  width_rolling_statistics,
                                                                  height_rolling_statistics).content)
