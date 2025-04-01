# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from trading_agent.models.inference import InferenceModel

# router = APIRouter()

# class InferenceRequest(BaseModel):
#     data: list

# class InferenceResponse(BaseModel):
#     predictions: list

# inference_model = InferenceModel()

# @router.post("/predict", response_model=InferenceResponse)
# async def predict(request: InferenceRequest):
#     try:
#         predictions = inference_model.predict(request.data)
#         return InferenceResponse(predictions=predictions)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))