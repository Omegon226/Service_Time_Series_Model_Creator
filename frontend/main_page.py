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
    bytes_data = uploaded_file.read()
    s = str(bytes_data, 'utf-8')
    data = StringIO(s)
    df = pd.read_csv(data)

    #if st.button('Create DataFrame'):
    #    pass

with tab_import_json:
    st.header("Import your JSON file here")
    uploaded_file = st.file_uploader("Choose a JSON file", accept_multiple_files=False)

    #if st.button('Create DataFrame'):
    #    pass

with tab_import_dict:
    st.header("Import your Data in Dict format here")
    dict_data_str = st.text_input('Dict/JSON like text', '{"a": [1, 2, 3], "b": [4, 5, 6]}')

    if st.button('Create DataFrame'):
        df = pd.DataFrame(json.loads(dict_data_str))

with tab_data_table:
    if df is None:
        st.header("No Data to print")
    else:
        st.header("Data table")
        st.dataframe(df)
