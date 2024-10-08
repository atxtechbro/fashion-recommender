from fastapi import FastAPI

from snazzy_closet.backend.api.user_routes import router as user_router
from snazzy_closet.backend.api.clothing_item_routes import router as clothing_item_router

app = FastAPI()

app.include_router(user_router, prefix="/api/v1")
app.include_router(clothing_item_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
