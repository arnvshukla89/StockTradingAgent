# Stock Trading Agent

This project is a comprehensive stock trading agent designed to facilitate data ingestion, feature engineering, model training, and inference for trading strategies. It leverages various technologies and frameworks to provide a robust solution for algorithmic trading.

## Project Structure

The project is organized into several directories, each serving a specific purpose:

- **src/**: Contains the source code for the trading agent.
  - **trading_agent/**: The main package that includes modules for configuration, logging, data ingestion, feature engineering, model training, and API services.
  - **airflow/**: Contains Airflow DAGs and setup for orchestrating workflows.
  - **kubernetes/**: Deployment configurations for Kubernetes.
  - **notebooks/**: Jupyter Notebooks for data exploration and model experimentation.
  - **data/**: Directory for storing raw, processed, and feature data.
  - **tests/**: Unit and integration tests for the application.
  - **scripts/**: Utility scripts for running training, inference, and monitoring.

## Features

- **Data Ingestion**: Fetches historical and real-time data from external sources (e.g., Polygon.io).
- **Feature Engineering**: Extracts and transforms features for model training, including technical and fundamental indicators.
- **Model Training**: Trains machine learning models using various algorithms, including XGBoost and generative AI.
- **Inference**: Provides a FastAPI service for real-time inference of trading strategies.
- **Monitoring**: Implements monitoring for model performance and data drift detection.
- **Experiment Tracking**: Uses MLflow for tracking experiments and managing model versions.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.8 or higher
- Poetry for dependency management
- Docker for containerization
- Airflow for workflow orchestration

## Getting Started

1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-trading-agent
   ```

2. Install dependencies:
   ```
   poetry install
   ```

3. Set up the Airflow environment:
   ```
   cd airflow
   docker-compose up
   ```

4. Run the training pipeline:
   ```
   python scripts/run_training.py
   ```

5. Access the FastAPI service for inference:
   ```
   uvicorn src/trading_agent/api.main:app --reload
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.