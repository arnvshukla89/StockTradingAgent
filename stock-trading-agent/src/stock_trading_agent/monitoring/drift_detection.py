# from sklearn.metrics import mutual_info_score
# import numpy as np

# class DriftDetector:
#     def __init__(self, threshold=0.1):
#         self.threshold = threshold

#     def detect_drift(self, reference_data, current_data):
#         if len(reference_data) == 0 or len(current_data) == 0:
#             raise ValueError("Reference and current data must not be empty.")

#         drift_scores = []
#         for feature in reference_data.columns:
#             score = self._calculate_drift(reference_data[feature], current_data[feature])
#             drift_scores.append((feature, score))

#         return [(feature, score) for feature, score in drift_scores if score > self.threshold]

#     def _calculate_drift(self, reference_feature, current_feature):
#         return mutual_info_score(reference_feature, current_feature)

# # Example usage:
# # detector = DriftDetector(threshold=0.1)
# # drifted_features = detector.detect_drift(reference_data, current_data)
# # print("Drifted features:", drifted_features)