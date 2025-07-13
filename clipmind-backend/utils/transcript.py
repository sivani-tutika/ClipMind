from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url: str) -> str:
    """
    Extracts the YouTube video ID from a full URL.
    Supports both youtube.com and youtu.be links.
    """
    match = re.search(
        r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
        url
    )
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

def fetch_transcript(video_url: str) -> str:
    """
    Fetches the transcript for a given YouTube video.
    Returns a single string of concatenated text entries.
    """
    video_id = extract_video_id(video_url)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        print(f"Fetched transcript for video ID: {video_id}")
        return ' '.join([entry['text'] for entry in transcript])
    except Exception as e:
        raise ValueError(f"Could not fetch transcript: {e}")
