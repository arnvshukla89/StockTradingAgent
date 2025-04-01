# import os
# import sys
# import joblib
# from src.trading_agent.models.inference import InferenceModel
# from src.trading_agent.mlflow_tracking.register_model import register_model

# def deploy_model(model_path, model_name):
#     if not os.path.exists(model_path):
#         print(f"Model path {model_path} does not exist.")
#         sys.exit(1)

#     # Load the trained model
#     model = joblib.load(model_path)
#     inference_model = InferenceModel(model)

#     # Register the model with MLflow
#     register_model(model_name, model_path)

#     print(f"Model {model_name} deployed successfully.")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python deploy_model.py <model_path> <model_name>")
#         sys.exit(1)

#     model_path = sys.argv[1]
#     model_name = sys.argv[2]
#     deploy_model(model_path, model_name)