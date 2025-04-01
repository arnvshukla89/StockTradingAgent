# from trading_agent.data_ingestion.historical_data import fetch_historical_data
# from trading_agent.data_ingestion.real_time_stream import start_real_time_stream
# from trading_agent.feature_engineering.features import extract_features
# from trading_agent.models.train import train_model
# from trading_agent.mlflow_tracking.mlflow_utils import log_experiment
# from trading_agent.data_tracking.sync_data import sync_data
# from trading_agent.monitoring.performance_metrics import evaluate_performance

# def training_pipeline():
#     # Step 1: Fetch historical data
#     historical_data = fetch_historical_data()

#     # Step 2: Start real-time data stream
#     real_time_data = start_real_time_stream()

#     # Step 3: Combine historical and real-time data
#     combined_data = historical_data.append(real_time_data)

#     # Step 4: Extract features from the combined data
#     features = extract_features(combined_data)

#     # Step 5: Train the model using the extracted features
#     model = train_model(features)

#     # Step 6: Log the experiment to MLflow
#     log_experiment(model)

#     # Step 7: Sync data with S3
#     sync_data()

#     # Step 8: Evaluate the model performance
#     performance_metrics = evaluate_performance(model)

#     return model, performance_metrics

# if __name__ == "__main__":
#     trained_model, metrics = training_pipeline()
#     print("Training completed. Model and metrics are ready.")