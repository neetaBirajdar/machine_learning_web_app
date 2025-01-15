from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api import detect_number_api, detect_draw_api
from fastapi.staticfiles import StaticFiles


app = FastAPI()
# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")


# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request})
                                  
                                    
app.include_router(detect_number_api.router)
app.include_router(detect_draw_api.router)





