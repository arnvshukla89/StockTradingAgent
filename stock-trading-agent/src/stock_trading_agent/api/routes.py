# from fastapi import APIRouter
# from .inference_service import InferenceService
# from .schemas import InferenceRequest, InferenceResponse

# router = APIRouter()

# @router.post("/inference", response_model=InferenceResponse)
# async def get_inference(request: InferenceRequest):
#     return await InferenceService.perform_inference(request)

# @router.get("/health")
# async def health_check():
#     return {"status": "healthy"}