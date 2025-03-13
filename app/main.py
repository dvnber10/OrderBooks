from fastapi import FastAPI
from app.controllers import user_controller
from app.database import engine, Base

Base.metadata.create_all(bind=engine)  # Crea las tablas si no existen

app = FastAPI()

app.include_router(user_controller.router, prefix="/api")
