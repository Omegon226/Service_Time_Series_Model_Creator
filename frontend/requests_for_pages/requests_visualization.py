import requests

HOST = "127.0.0.1"
PORT = 8000


class RequestsVisualization:
    @staticmethod
    def request_get_all_params():
        return requests.get(f"http://{HOST}:{PORT}/data_manipulation/get_all_params_of_time_series/").json()[
            "all_params"]

    @staticmethod
    def request_plot(params, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "params": params}

        return requests.post(f"http://{HOST}:{PORT}/visualise_plot_of_data/create_plot_of_all_data/",
                             json=json_data)

    @staticmethod
    def request_histogram(params, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "params": params}

        return requests.post(f"http://{HOST}:{PORT}/visualise_hist_of_data/create_hist_of_all_data/",
                             json=json_data)

    @staticmethod
    def request_boxplot(params, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "params": params}

        return requests.post(f"http://{HOST}:{PORT}/visualise_boxplot_of_data/create_boxplot_of_all_data/",
                             json=json_data)

    @staticmethod
    def request_violinplot(params, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "params": params}

        return requests.post(f"http://{HOST}:{PORT}/visualise_violinplot_of_data/create_violinplot_of_all_data/",
                             json=json_data)

    @staticmethod
    def request_corr_heatmap(method, params, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "params": params}

        if method == "Spearman":
            return requests.post(f"http://{HOST}:{PORT}/visualise_corrheatmap_of_data/create_corrheatmap_spearman_of_all_data/",
                                 json=json_data)
        elif method == "Pearson":
            return requests.post(f"http://{HOST}:{PORT}/visualise_corrheatmap_of_data/create_corrheatmap_pearson_of_all_data/",
                                 json=json_data)

    @staticmethod
    def request_rolling_average(window_size, params, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "params": params, "window_size": window_size}

        return requests.post(f"http://{HOST}:{PORT}/visualize_rolling_statistics_of_data/create_rolling_statistics_of_selected_data/",
                             json=json_data)

    @staticmethod
    def request_rolling_statistics(window_size, fig_weights, fig_height):
        json_data = {"fig_weights": fig_weights, "fig_height": fig_height, "window_size": window_size}

        return requests.post(f"http://{HOST}:{PORT}/visualize_rolling_average_of_data/create_rolling_average_of_selected_data/",
                             json=json_data)
