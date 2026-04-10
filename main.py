from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.get("/getSettings")
async def get_settings(idInstance: str, apiToken: str):
    url = f"https://api.green-api.com/waInstance{idInstance}/getSettings/{apiToken}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response text: {response.text}")

    try:
        return response.json()
    except Exception as e:
        logger.error(f"Error parsing JSON: {e}")
        return {"error": "Invalid response from API", "status": response.status_code, "text": response.text}


@app.get("/getStateInstance")
async def get_state(idInstance: str, apiToken: str):
    url = f"https://api.green-api.com/waInstance{idInstance}/getStateInstance/{apiToken}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response text: {response.text}")

    try:
        return response.json()
    except Exception as e:
        logger.error(f"Error parsing JSON: {e}")
        return {"error": "Invalid response from API", "status": response.status_code, "text": response.text}


@app.post("/sendMessage")
async def send_message(idInstance: str, apiToken: str, chatId: str, message: str):
    url = f"https://api.green-api.com/waInstance{idInstance}/sendMessage/{apiToken}"

    payload = {
        "chatId": chatId,
        "message": message
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)

    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response text: {response.text}")

    try:
        return response.json()
    except Exception as e:
        logger.error(f"Error parsing JSON: {e}")
        return {"error": "Invalid response from API", "status": response.status_code, "text": response.text}


@app.post("/sendFileByUrl")
async def send_file(idInstance: str, apiToken: str, chatId: str, fileUrl: str):
    url = f"https://api.green-api.com/waInstance{idInstance}/sendFileByUrl/{apiToken}"

    payload = {
        "chatId": chatId,
        "urlFile": fileUrl,
        "fileName": "file"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)

    logger.info(f"Status: {response.status_code}")
    logger.info(f"Response text: {response.text}")

    try:
        return response.json()
    except Exception as e:
        logger.error(f"Error parsing JSON: {e}")
        return {"error": "Invalid response from API", "status": response.status_code, "text": response.text}