import streamlit as st
from io import StringIO
import json
import pandas as pd

st.title("Import Data")

df = None

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
        st.header("Data table")
        st.dataframe(df)


st.markdown("----")
st.title("Data Work")

tab_change_main_param, tab_create_new_param, tab_delete_nan, tab_data_manipulation = \
    st.tabs(["Change Main Parameter", "Create New Parameter", "Change NAN Data", "Data Manipulation"])


with tab_change_main_param:
    if st.button('Send Request for Changing Main Parameter'):
        st.write('ABOBA')

with tab_create_new_param:
    if st.button('Send Request for Creating New Parameter'):
        st.write('ABOBA')

with tab_delete_nan:
    if st.button('Send Request for Changing NAN Data'):
        st.write('ABOBA')

with tab_data_manipulation:
    if st.button('Send Request for Data Manipulation'):
        st.write('ABOBA')







st.markdown("----")
st.title("Visualization")

tab_timeseries_plot, tab_histogram, tab_boxplot, tab_violinplot, tab_corr_heatmap, tab_rolling_average, \
    tab_rolling_statistics = st.tabs(["Timeseries Plot", "Histogram", "Boxplot", "Violinplot", "Correlation Heatmap",
                                      "Rolling Average", "Rolling Statistics"])

with tab_timeseries_plot:
    if st.button('Create Timeseries Plot'):
        st.write('ABOBA')

with tab_histogram:
    if st.button('Create Histogram'):
        st.write('ABOBA')

with tab_boxplot:
    if st.button('Create Boxplot'):
        st.write('ABOBA')

with tab_violinplot:
    if st.button('Create Violinplot'):
        st.write('ABOBA')

with tab_corr_heatmap:
    if st.button('Create Correlation Heatmap'):
        st.write('ABOBA')

with tab_rolling_average:
    if st.button('Create Rolling Average'):
        st.write('ABOBA')

with tab_rolling_statistics:
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







