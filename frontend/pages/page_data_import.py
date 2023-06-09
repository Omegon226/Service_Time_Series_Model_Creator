import streamlit as st

from frontend.requests_for_pages.requests_data_import import RequestsDataImport


df = None


st.title("Import Data")

tab_import_csv, tab_import_json, tab_import_dict, tab_data_table = \
    st.tabs(["Import data from CSV", "Import data from JSON", "Import data from Dict", "Data Table"])


with tab_import_csv:
    st.header("Import your CSV file here")
    uploaded_file = st.file_uploader("Choose a CSV file", accept_multiple_files=False, type="csv")

    if st.button('Create Data from CSV'):
        RequestsDataImport.request_set_data_from_csv(uploaded_file)

with tab_import_json:
    st.header("Import your JSON file here")
    uploaded_file = st.file_uploader("Choose a JSON file", accept_multiple_files=False, type="json")

    if st.button('Create Data from JSON'):
        RequestsDataImport.request_set_data_from_json(uploaded_file)

with tab_import_dict:
    st.header("Import your Data in Dict format here")
    dict_data_str = st.text_input('Dict/JSON like text', '{"a": [1, 2, 3], "b": [4, 5, 6]}')

    if st.button('Create Data from Dict'):
        RequestsDataImport.request_set_data_from_dict(dict_data_str)

with tab_data_table:
    df = RequestsDataImport.request_get_df()

    if df is None:
        st.header("No Data to print")
    else:
        st.header("Data Table")
        st.dataframe(df)
