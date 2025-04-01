# import pytest
# from src.trading_agent.models.inference import InferenceModel

# @pytest.fixture
# def inference_model():
#     model = InferenceModel()
#     model.load_model("path/to/model")  # Adjust the path as necessary
#     return model

# def test_inference_valid_input(inference_model):
#     input_data = {"feature1": 1.0, "feature2": 2.0}  # Example input
#     prediction = inference_model.predict(input_data)
#     assert prediction is not None
#     assert isinstance(prediction, float)  # Assuming the model returns a float

# def test_inference_invalid_input(inference_model):
#     input_data = {"feature1": "invalid", "feature2": 2.0}  # Invalid input
#     with pytest.raises(ValueError):
#         inference_model.predict(input_data)

# def test_inference_model_loaded(inference_model):
#     assert inference_model.is_model_loaded()  # Assuming this method checks if the model is loaded