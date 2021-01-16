from decouple import AutoConfig

from constants import SRC_ROOT

# Settings.ini
config = AutoConfig(search_path=SRC_ROOT)

API_KEY = config('API_KEY', None)
CHANNEL_ID = config('CHANNELID', None)
