# from typing import Any, Dict
# import joblib
# import numpy as np

# class InferenceModel:
#     def __init__(self, model_path: str):
#         self.model = joblib.load(model_path)

#     def predict(self, features: np.ndarray) -> Any:
#         return self.model.predict(features)

#     def predict_proba(self, features: np.ndarray) -> np.ndarray:
#         return self.model.predict_proba(features)

#     def get_model_info(self) -> Dict[str, Any]:
#         return {
#             "model_type": type(self.model).__name__,
#             "model_params": self.model.get_params()
#         }