import streamlit as st
import pandas as pd
import json

from frontend.requests_for_pages.requests_data_work import RequestsDataWork


df_statistics = None
params_of_df = RequestsDataWork.request_get_all_params()


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
    df_statistics = RequestsDataWork.request_get_all_params_statistics()

    if df_statistics is None:
        st.header("No Data to print")
    else:
        st.header("Data Statistics")
        st.dataframe(df_statistics)
