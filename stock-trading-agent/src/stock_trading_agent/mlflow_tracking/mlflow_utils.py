# from mlflow import log_param, log_metric, start_run, end_run

# def log_experiment_params(params):
#     """
#     Log parameters for the current MLflow run.
    
#     Args:
#         params (dict): A dictionary of parameters to log.
#     """
#     with start_run():
#         for key, value in params.items():
#             log_param(key, value)

# def log_experiment_metrics(metrics):
#     """
#     Log metrics for the current MLflow run.
    
#     Args:
#         metrics (dict): A dictionary of metrics to log.
#     """
#     with start_run():
#         for key, value in metrics.items():
#             log_metric(key, value)

# def get_experiment_id(experiment_name):
#     """
#     Get the experiment ID for a given experiment name.
    
#     Args:
#         experiment_name (str): The name of the experiment.
    
#     Returns:
#         str: The experiment ID.
#     """
#     from mlflow import get_experiment_by_name
#     experiment = get_experiment_by_name(experiment_name)
#     return experiment.experiment_id if experiment else None

# def log_model_info(model_name, model_version):
#     """
#     Log model information for the current MLflow run.
    
#     Args:
#         model_name (str): The name of the model.
#         model_version (str): The version of the model.
#     """
#     with start_run():
#         log_param("model_name", model_name)
#         log_param("model_version", model_version)