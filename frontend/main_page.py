import streamlit as st
from io import StringIO
import json
import pandas as pd

st.title("Import Data")

df = None
params_of_df = ["PARAM_1", "PARAM_2", "PARAM_3", "PARAM_4", "PARAM_5"]


tab_import_csv, tab_import_json, tab_import_dict, tab_data_table = \
    st.tabs(["Import data from CSV", "Import data from JSON", "Import data from Dict", "Data Table"])


with tab_import_csv:
    st.header("Import your CSV file here")
    uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False)

    if st.button('Create Data from CSV'):
        bytes_data = uploaded_file.read()
        s = str(bytes_data, 'utf-8')
        data = StringIO(s)
        df = pd.read_csv(data)

with tab_import_json:
    st.header("Import your JSON file here")
    uploaded_file = st.file_uploader("Choose a JSON file", accept_multiple_files=False)

    if st.button('Create Data from JSON'):
        bytes_data = uploaded_file.read()
        s = str(bytes_data, 'utf-8')
        data = StringIO(s)
        df = pd.read_json(data)

with tab_import_dict:
    st.header("Import your Data in Dict format here")
    dict_data_str = st.text_input('Dict/JSON like text', '{"a": [1, 2, 3], "b": [4, 5, 6]}')

    if st.button('Create Data from Dict'):
        df = pd.DataFrame(json.loads(dict_data_str))

with tab_data_table:
    if df is None:
        st.header("No Data to print")
    else:
        st.header("Data Table")
        st.dataframe(df)


st.markdown("----")
st.title("Data Work")

tab_change_main_param, tab_change_data_params, tab_create_new_param, tab_delete_nan, tab_get_statistics = \
    st.tabs(["Change Main Parameter", "Change Data Parameters", "Create New Parameter", "Change NAN Data",
             "Get Statistics"])


with tab_change_main_param:
    change_main_param_option = st.selectbox(
        "Set Main Parameter",
        params_of_df)
    if st.button('Send Request for Changing Main Parameter'):
        st.write('ABOBA')

with tab_change_data_params:
    change_data_params_selected = st.multiselect(
        'Set Data Parameters',
        params_of_df,
        params_of_df)
    if st.button('Send Request for Changing Data Parameters'):
        st.write('ABOBA')

with tab_create_new_param:
    create_new_param_option = st.selectbox(
        "Set what Parameter to Create",
        ["mean", "median", "range", "std"])
    if st.button('Send Request for Creating New Parameter'):
        st.write('ABOBA')

with tab_delete_nan:
    delete_nan_option = st.selectbox(
        "Set Type of Deleting NAN Values",
        ("drop rows", "zero", "mean", "median"))
    if st.button('Send Request for Changing NAN Data'):
        st.write('ABOBA')

with tab_get_statistics:
    if df is None:
        st.header("No Data to print")
    else:
        st.header("Data Statistics")
        st.dataframe(df.describe())


st.markdown("----")
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


st.markdown("----")
st.title("ML Pipeline Creation")

scalers_selected = st.multiselect(
    'Set Scalers for ML Pipelines',
    ['Max ABS Scaler', 'Min Max Scaler', 'Standard Scaler'],
    ['Min Max Scaler'])

st.write('You selected:', scalers_selected)

ml_models_selected = st.multiselect(
    'Set ML Models for ML Pipelines',
    ["DNN", "RNN", "LSTM", "GRU"],
    ["RNN", "LSTM"])

st.write('You selected:', ml_models_selected)

tests_selected = st.multiselect(
    'Set Tests for testing ML Pipelines',
    ['MSE', 'RMSE', 'R^2', 'MAE'],
    ['MSE', 'RMSE', 'R^2'])

st.write('You selected:', tests_selected)

if st.button('Create ML Pipelines'):
    st.write('ABOBA')


st.markdown("----")
st.title("Get Best ML Pipelines")

amount_best_models = st.number_input('Insert count of Best ML Pipelines', step=1, value=1, min_value=1)
st.write('The current number is ', amount_best_models)

if st.button('Get Best ML Pipelines'):
    st.write('ABOBA')

