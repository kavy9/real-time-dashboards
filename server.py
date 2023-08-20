from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import uvicorn
from googleapiclient.discovery import build
from google.oauth2 import service_account

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

Key_path = 'sample.json'
TABLE_ID = 149579298
credentials = service_account.Credentials.from_service_account_file(Key_path)
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/analytics/readonly'])

# Set up Jinja2 templates
templates = Jinja2Templates(directory="static")


@app.get("/", response_class=HTMLResponse)
async def serve_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/real-time-api-page')
async def real_time(info: Request):
    req_info = await info.json()
    with build('analytics', 'v3', credentials=credentials) as service:
        realtime_data = service.data().realtime().get(
            ids=f'ga:{TABLE_ID}',
            dimensions='rt:source,rt:medium,rt:campaign',
            metrics='rt:activeUsers',
            filters=f'ga:PagePath=~{req_info.page}'
        ).execute()

        return {"source_medium": realtime_data['rows'], "total": realtime_data['totalsForAllResults']['rt:activeUsers']}

@app.post('/real-time-api-minutesAgo')
async def real_time(info: Request):
    req_info = await info.json()
    with build('analytics', 'v3', credentials=credentials) as service:
        realtime_data = service.data().realtime().get(
            ids=f'ga:{TABLE_ID}',
            dimensions='rt:source,rt:medium,rt:campaign',
            metrics='rt:activeUsers',
            filters=f'ga:PagePath=~{req_info.page}'
        ).execute()

        return {"source_medium": realtime_data['rows'], "total": realtime_data['totalsForAllResults']['rt:activeUsers']}



if __name__ == "__main__":
    print("Running it on the local host")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
