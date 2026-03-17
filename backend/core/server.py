
from fastapi import FastAPI

from api import router


def run_server() -> FastAPI:
    app_ = FastAPI(title="Online Store")
    app_.include_router(router)
    return app_
