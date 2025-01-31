from fastapi import HTTPException
from pytube import exceptions
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound


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
            video_id, languages=["pt", "en"]
        )

        output = ""
        for entry in transcript:
            output += f"{entry['text']}\n"

        return output
    except NoTranscriptFound:
        raise HTTPException(
            status_code=404,
            detail=f"This video does not have a transcript available.\nID: {video_id}",
        )
    except exceptions.VideoError:
        raise HTTPException(status_code=500, detail="Error accessing the video")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
