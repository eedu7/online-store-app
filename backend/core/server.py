from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router
from core.config import config


def make_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.CORS_ALLOW_ORIGINS,
        allow_credentials=config.CORS_ALLOW_CREDENTIALS,
        allow_methods=config.CORS_ALLOW_METHODS,
        allow_headers=config.CORS_ALLOW_HEADERS,
    )


def run_server() -> FastAPI:
    app_ = FastAPI(
        title="Online Store",
    )
    app_.include_router(router)
    make_middleware(app_)
    return app_
