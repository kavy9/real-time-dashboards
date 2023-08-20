import finnhub
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="static")

sample_data = [
    {"source": "Source1", "medium": "Medium1", "campaign": "Campaign1", "number": 10},
    {"source": "Source2", "medium": "Medium2", "campaign": "Campaign2", "number": 20},
    # Add more data as needed
]

@app.get("/", response_class=HTMLResponse)
async def serve_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/real-time-api')
async def real_time():
    return sample_data
    # return [['a', 'b', 'c', 1],
    #         ['t', 'y', 'u', 3]]


if __name__ == "__main__":
    print("Running it on the local host")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
