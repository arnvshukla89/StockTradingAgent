# from fastapi import FastAPI
# from trading_agent.api.routes import router as api_router
# from trading_agent.config import settings

# app = FastAPI(title="Stock Trading Agent API", version="1.0")

# @app.on_event("startup")
# async def startup_event():
#     # Initialize any resources needed at startup
#     pass

# @app.on_event("shutdown")
# async def shutdown_event():
#     # Clean up resources on shutdown
#     pass

# app.include_router(api_router, prefix=settings.API_PREFIX)