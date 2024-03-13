from fastapi import FastAPI

from src.api import api_router

from prometheus_fastapi_instrumentator import Instrumentator


def create_app():
    application = FastAPI()
    application.include_router(api_router)
    Instrumentator().instrument(application).expose(application)
    return application


app = create_app()
