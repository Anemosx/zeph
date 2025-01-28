import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import playlist_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


zeph_app: FastAPI = FastAPI(
    title="Zeph",
    version=os.getenv("VERSION", "0.0.1"),
    lifespan=lifespan,
)
zeph_app.mount("/static", StaticFiles(directory="static"), name="static")
zeph_app.include_router(playlist_router)


if __name__ == "__main__":
    uvicorn.run("app.main:zeph_app", host="0.0.0.0", port=8088)
