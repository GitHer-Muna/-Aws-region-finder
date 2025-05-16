from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.country_check import validate_country
from app.services.aws_data import get_aws_regions_by_country

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@router.post("/check", response_class=HTMLResponse)
async def form_post(request: Request, country: str = Form(...)):
    if not await validate_country(country):
        return templates.TemplateResponse("form.html", {"request": request, "error": "Invalid country."})
    regions = await get_aws_regions_by_country(country)
    return templates.TemplateResponse("result.html", {"request": request, "country": country, "regions": regions})
