# from mlflow import log_artifact, log_params, log_metrics, start_run

# def register_model(model_uri: str, model_name: str, tags: dict = None):
#     """
#     Registers a model in MLflow.

#     Parameters:
#     - model_uri: The URI of the model to register.
#     - model_name: The name to assign to the registered model.
#     - tags: Optional dictionary of tags to associate with the model.

#     Returns:
#     - The registered model version.
#     """
#     with start_run():
#         # Log parameters and tags if provided
#         if tags:
#             for key, value in tags.items():
#                 log_params({key: value})

#         # Register the model
#         model_version = mlflow.register_model(model_uri=model_uri, name=model_name)

#         # Log the model version
#         log_metrics({"model_version": model_version.version})

#     return model_version