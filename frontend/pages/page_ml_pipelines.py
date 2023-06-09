import streamlit as st


df = None
params_of_df = ["PARAM_1", "PARAM_2", "PARAM_3", "PARAM_4", "PARAM_5"]


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