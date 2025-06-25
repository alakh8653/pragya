from fastapi import FastAPI
from backend.config.settings import settings
from backend.src import auth, courses, analytics, assessments, assignments, messaging, notifications, payments, users

app = FastAPI(title=settings.app_name)

for module in [auth, courses, analytics, assessments, assignments, messaging, notifications, payments, users]:
    app.include_router(module.router)

@app.get('/')
async def root():
    return {"message": "Welcome to the Online Learning Platform"}
