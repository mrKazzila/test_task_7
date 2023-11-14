from fastapi import FastAPI

from api.forms.router import router as forms_router
from api.healthcheck.router import router as healthcheck_router


def routers_setup(app: FastAPI) -> None:
    app.include_router(forms_router)
    app.include_router(healthcheck_router)
