from typing import Union
from fastapi import FastAPI, APIRouter
from routers import mortgage, deposits

app = FastAPI()

v1_router = APIRouter(prefix="/api/v1")

v1_router.include_router(mortgage.router)
v1_router.include_router(deposits.router)
app.include_router(v1_router)
