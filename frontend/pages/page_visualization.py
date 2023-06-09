import streamlit as st


df = None
params_of_df = ["PARAM_1", "PARAM_2", "PARAM_3", "PARAM_4", "PARAM_5"]


st.title("Visualization")

tab_timeseries_plot, tab_histogram, tab_boxplot, tab_violinplot, tab_corr_heatmap, tab_rolling_average, \
    tab_rolling_statistics = st.tabs(["Timeseries Plot", "Histogram", "Boxplot", "Violinplot", "Correlation Heatmap",
                                      "Rolling Average", "Rolling Statistics"])


with tab_timeseries_plot:
    params_for_timeseries_plot_selected = st.multiselect(
        'Set Parameters to Timeseries Plot',
        params_of_df,
        params_of_df)
    if st.button('Create Timeseries Plot'):
        st.write('ABOBA')

with tab_histogram:
    params_for_histogram_selected = st.multiselect(
        'Set Parameters to Histogram',
        params_of_df,
        params_of_df)
    if st.button('Create Histogram'):
        st.write('ABOBA')

with tab_boxplot:
    params_for_boxplot_selected = st.multiselect(
        'Set Parameters to Boxplot',
        params_of_df,
        params_of_df)
    if st.button('Create Boxplot'):
        st.write('ABOBA')

with tab_violinplot:
    params_for_violinplot_selected = st.multiselect(
        'Set Parameters to Violinplot',
        params_of_df,
        params_of_df)
    if st.button('Create Violinplot'):
        st.write('ABOBA')

with tab_corr_heatmap:
    correlation_option = st.selectbox(
        "Correlation calculation method",
        ("Pearson", "Spearman"))
    params_for_corr_heatmap_selected = st.multiselect(
        'Set Parameters to plot Correlation Heatmap',
        params_of_df,
        params_of_df)
    if st.button('Create Correlation Heatmap'):
        st.write('ABOBA')

with tab_rolling_average:
    window_size_rolling_average = st.number_input('Insert window size for Rolling Average',
                                                  step=1, value=15, min_value=1)
    if st.button('Create Rolling Average'):
        st.write('ABOBA')

with tab_rolling_statistics:
    window_size_rolling_statistics = st.number_input('Insert window size fro Rolling Statistics',
                                                     step=1, value=15, min_value=1)
    params_for_rolling_statistics_selected = st.multiselect(
        'Set Parameters to plot Rolling Statistics',
        params_of_df,
        params_of_df)
    if st.button('Create Rolling Statistics'):
        st.write('ABOBA')