import streamlit as st
import pandas as pd
import json


df = pd.DataFrame(json.loads('{"a": [1, 2, 3], "b": [4, 5, 6]}'))
params_of_df = ["PARAM_1", "PARAM_2", "PARAM_3", "PARAM_4", "PARAM_5"]


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