# def evaluate_model(predictions, ground_truth):
#     """
#     Evaluate the model's predictions against the ground truth values.

#     Parameters:
#     predictions (list): The predicted values from the model.
#     ground_truth (list): The actual values to compare against.

#     Returns:
#     dict: A dictionary containing evaluation metrics.
#     """
#     from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#     accuracy = accuracy_score(ground_truth, predictions)
#     precision = precision_score(ground_truth, predictions, average='weighted')
#     recall = recall_score(ground_truth, predictions, average='weighted')
#     f1 = f1_score(ground_truth, predictions, average='weighted')

#     return {
#         'accuracy': accuracy,
#         'precision': precision,
#         'recall': recall,
#         'f1_score': f1
#     }