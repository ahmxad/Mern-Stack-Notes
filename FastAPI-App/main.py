from fastapi import FastAPI
from routes.users import router as user_router

app = FastAPI(title="User Service")

app.include_router(user_router)