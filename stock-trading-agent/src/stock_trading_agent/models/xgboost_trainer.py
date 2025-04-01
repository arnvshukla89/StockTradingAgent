# from xgboost import XGBClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import pandas as pd

# class XGBoostTrainer:
#     def __init__(self, params=None):
#         self.model = XGBClassifier(**(params if params else {}))
    
#     def train(self, X, y):
#         X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
#         self.model.fit(X_train, y_train)
#         y_pred = self.model.predict(X_val)
#         accuracy = accuracy_score(y_val, y_pred)
#         return accuracy
    
#     def predict(self, X):
#         return self.model.predict(X)
    
#     def save_model(self, filepath):
#         self.model.save_model(filepath)
    
#     def load_model(self, filepath):
#         self.model.load_model(filepath)