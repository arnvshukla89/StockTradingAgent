import os
# from dotenv import load_dotenv

# load_dotenv()
class Config:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.api_key = os.getenv('API_KEY')
        self.db_url = os.getenv('DATABASE_URL')
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')
        self.model_path = os.getenv('MODEL_PATH', './models')
        self.data_path = os.getenv('DATA_PATH', './data')
        self.port = int(os.getenv('PORT', 8000))

    def __repr__(self):
        return f"<Config(environment={self.environment}, log_level={self.log_level}, port={self.port})>"

config = Config()