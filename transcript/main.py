from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transcript import service

app = FastAPI()
app.mount("/web", StaticFiles(directory="transcript/web"), name="web")


# Pydantic model for incoming request data
class VideoURL(BaseModel):
    url: str


@app.get("/")
async def index():
    # Just returns a simple message or index page in the future
    with open("transcript/web/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
        return HTMLResponse(content=html_content)


@app.post("/transcribe")
async def transcribe_video(video: VideoURL):
    url = video.url

    response = service.get_video_transcript(url)

    return JSONResponse(content={"transcript": response})
