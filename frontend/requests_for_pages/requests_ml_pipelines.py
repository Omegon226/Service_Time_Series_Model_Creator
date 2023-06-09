import requests

HOST = "127.0.0.1"
PORT = 8000


SCALERS = {'Max ABS Scaler': 'max_abs_scaler', 'Min Max Scaler': 'min_max_scaler', 'Standard Scaler': 'standard_scaler'}
TESTS = {'MSE': 'mse', 'RMSE': 'rmse', 'R^2': 'r2', 'MAE': 'mae'}
ML_MODELS = {
    "DNN 100-200": {"model": "keras_dense", "hidden_layers_size": [100, 200], "hidden_layers_activation": ["relu",
                                                                                                           "relu"],
                    "amount_of_params": 5, "horizon_for_prediction": 100, "horizon_of_prediction": 10},
    "RNN 50": {"model": "keras_rnn", "hidden_layers_size": [50], "hidden_layers_activation": ["relu"],
               "amount_of_params": 5, "horizon_for_prediction": 150, "horizon_of_prediction": 20},
    "LSTM 50-50": {"model": "keras_lstm", "hidden_layers_size": [50, 50], "hidden_layers_activation": ["relu",
                                                                                                        "relu"],
                   "amount_of_params": 5, "horizon_for_prediction": 150, "horizon_of_prediction": 15},
    "GRU 100": {"model": "keras_gru", "hidden_layers_size": [100], "hidden_layers_activation": ["relu"],
                "amount_of_params": 5, "horizon_for_prediction": 75, "horizon_of_prediction": 10}
}


class RequestsMLPipelines:
    @staticmethod
    def request_get_all_params():
        return requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_all_params_of_time_series/").json()[
            "all_params"]

    @staticmethod
    def request_get_amount_of_ml_pipelines_dirs():
        return requests.get(f"http://{HOST}:{PORT}/pipelines_creator/get_amount_of_ml_pipelines_dirs/").json()[
            "amount_of_dirs"]

    @staticmethod
    def request_for_ml_pipelines_creation(scalers, models, tests):
        scalers_new = []
        models_new = {}
        tests_new = []

        for i in scalers:
            scalers_new += [SCALERS[i]]
        counter = 1
        for i in models:
            models_new[f"model_{counter}"] = ML_MODELS[i]
            counter += 1
        for i in tests:
            tests_new += [TESTS[i]]

        json_data = {"scalers": scalers_new, "ml_models": models_new, "tests": tests_new}

        requests.post(f"http://{HOST}:{PORT}/pipelines_creator/create_pipelines/", json=json_data)
        return "Success"

    @staticmethod
    def request_for_finding_best_ml_pipelines(amount_best_models, number_of_dir):
        json_data = {"amount": amount_best_models, "nom_of_pipeline_creation": number_of_dir}

        result = requests.post(f"http://{HOST}:{PORT}/pipelines_creator/get_best_pipelines/", params=json_data)
        return list(result.json()["best_pipelines_by_metric"].keys())
