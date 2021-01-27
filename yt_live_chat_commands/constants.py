from pathlib import Path

SRC_ROOT = Path(__file__).resolve().parent
REPO_ROOT = SRC_ROOT.parent

SOUNDS_SRC = SRC_ROOT / "sounds"

SOUNDS_CMD = {x.stem: x for x in SOUNDS_SRC.glob("**/*")}

VALID_CMD = list(SOUNDS_CMD.keys()) + ["led"]

CHAR_CMD = "!"

VIEWER_DIR = SRC_ROOT / "data"
VIEWER_FILE = "viewer.csv"
CACHE_FILE = ".cache"

YT_API_USER_DATA_ENDPOINT = 'https://www.googleapis.com/youtube/v3/search'
YT_API_VIDEOS_DATA_ENDPOINT = 'https://www.googleapis.com/youtube/v3/videos'
YT_API_LIVE_DATA_ENDPOINT = 'https://youtube.googleapis.com/youtube/v3/liveBroadcasts'
YT_API_CHAT_DATA_ENDPOINT = 'https://www.googleapis.com/youtube/v3/liveChat/messages'
