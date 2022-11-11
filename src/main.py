from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .core.config import settings
from .api import router


def include_router(app):
    app.include_router(router)


def add_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME)
    include_router(app)
    add_middleware(app)
    return app


app = start_application()
