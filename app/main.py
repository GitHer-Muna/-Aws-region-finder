from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import web

app = FastAPI(title="AWS Region Finder")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(web.router)
