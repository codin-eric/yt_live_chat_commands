from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parent
REPO_ROOT = SRC_ROOT.parent

SOUNDS_SRC = SRC_ROOT / "sounds"

SOUNDS_CMD = {x.stem: x for x in SOUNDS_SRC.glob("**/*")}

CHAR_CMD = "!"


YT_API_USER_DATA_ENDPOINT = 'https://www.googleapis.com/youtube/v3/search'
YT_API_VIDEOS_DATA_ENDPOINT = 'https://www.googleapis.com/youtube/v3/videos'
YT_API_CHAT_DATA_ENDPOINT = 'https://www.googleapis.com/youtube/v3/liveChat/messages'
