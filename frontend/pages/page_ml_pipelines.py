import streamlit as st

from frontend.requests_for_pages.requests_ml_pipelines import RequestsMLPipelines, SCALERS, ML_MODELS, TESTS


df = None
params_of_df = RequestsMLPipelines.request_get_all_params()


def create_all_combinations_of_ml_pipelines(scalers, ml_models):
    combinations = []
    for i in scalers:
        for j in ml_models:
            combinations += [str(i) + " ⇔ " + str(j)]

    return combinations


st.title("ML Pipeline Creation")

scalers_selected = st.multiselect(
    'Set Scalers for ML Pipelines',
    SCALERS,
    ['Min Max Scaler'])

ml_models_selected = st.multiselect(
    'Set ML Models for ML Pipelines',
    ML_MODELS,
    ["RNN 50", "LSTM 50-50"])

tests_selected = st.multiselect(
    'Set Tests for testing ML Pipelines',
    TESTS,
    ['MSE', 'RMSE', 'R^2'])

st.write('All combinations for ML Pipelines:  ', ":red[", "  |  ".join(
    create_all_combinations_of_ml_pipelines(scalers_selected, ml_models_selected)), "]")

if st.button('Create ML Pipelines'):
    result = RequestsMLPipelines.request_for_ml_pipelines_creation(scalers_selected, ml_models_selected, tests_selected)
    st.subheader(f"Result: :green[{result}]")

st.markdown("----")
st.title("Get Best ML Pipelines")

number_of_dir = st.slider('Dir for Searching', 1, RequestsMLPipelines.request_get_amount_of_ml_pipelines_dirs(), 1)
amount_best_models = st.number_input('Insert count of Best ML Pipelines', step=1, value=1, min_value=1)

if st.button('Get Best ML Pipelines'):
    best_models = RequestsMLPipelines.request_for_finding_best_ml_pipelines(amount_best_models, number_of_dir)

    st.subheader(f"Best models: :green[{',  '.join(best_models)}]")
