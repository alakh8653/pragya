from fastapi import FastAPI

from backend.config.settings import settings
from backend.src import (
    analytics,
    assessments,
    assignments,
    auth,
    courses,
    messaging,
    notifications,
    payments,
    users,
)


def create_app() -> FastAPI:
    """Build and configure the FastAPI application."""

    application = FastAPI(title=settings.app_name)

    for module in [
        auth,
        courses,
        analytics,
        assessments,
        assignments,
        messaging,
        notifications,
        payments,
        users,
    ]:
        application.include_router(module.router)

    @application.get('/')
    async def root():
        return {"message": "Welcome to the Online Learning Platform"}

    return application


app = create_app()
