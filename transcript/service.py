from fastapi import HTTPException
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound
from pytube.exceptions import PytubeError, RegexMatchError, LiveStreamError

from transcript.config import HTTP_PROXY, HTTPS_PROXY

proxy = {
    "http": HTTP_PROXY,
    "https": HTTPS_PROXY,
}


def _get_video_id(url):
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

    if "v=" in url:
        return url.split("v=")[1].split("&")[0]

    return url.split("/")[-1]


def get_video_transcript(url: str) -> str:
    try:
        video_id = _get_video_id(url)

        if not video_id or len(video_id) < 5:
            raise HTTPException(
                status_code=400, detail="Invalid URL or video ID not found"
            )

        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=["pt", "en"], proxies=proxy
        )

        output = ""
        for entry in transcript:
            output += f"{entry['text']}\n"

        return output
    except NoTranscriptFound:
        raise HTTPException(
            status_code=404,
            detail=f"Transcript not found for video.\nID: {video_id}",
        )
    except PytubeError as e:
        raise HTTPException(
            status_code=500, detail=f"Error accessing the video: {str(e)}"
        )
    except RegexMatchError as e:
        raise HTTPException(status_code=400, detail=f"URL error: {str(e)}")
    except LiveStreamError as e:
        raise HTTPException(
            status_code=404,
            detail="Error: The video is a live stream and does not have a transcript available.",
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
