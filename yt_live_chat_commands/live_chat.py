import requests
import logging
import simpleaudio as sa
from time import sleep
from cfg import API_KEY, CHANNEL_ID, RASPI_HOST
from constants import (
    YT_API_USER_DATA_ENDPOINT,
    YT_API_VIDEOS_DATA_ENDPOINT,
    YT_API_CHAT_DATA_ENDPOINT,
    VALID_CMD,
    SOUNDS_CMD,
    CHAR_CMD
)

logger = logging.getLogger(__name__)


class live_chat():
    def __init__(self):
        """Search the chat_id by user_id
        """
        params = {
            'part': 'id',
            'key': API_KEY,
            'channelId': CHANNEL_ID,
            'eventType': 'live',
            'type': 'video',
            'order': 'viewCount',
            'fields': 'items(id(videoId))'
        }

        r = requests.get(YT_API_USER_DATA_ENDPOINT,
                         headers=None, params=params).json()

        vID = r.get('items')[0].get('id').get('videoId')

        params = {
            'part': 'liveStreamingDetails,statistics,snippet',
            'key': API_KEY,
            'id': vID,
            'fields': 'items(id,liveStreamingDetails' +
            '(activeLiveChatId,concurrentViewers,actualStartTime),' +
            'snippet(channelId,channelTitle,description,liveBroadcastContent,' +
            'publishedAt,thumbnails,title),statistics)'
        }

        r = requests.get(YT_API_VIDEOS_DATA_ENDPOINT,
                         headers=None, params=params).json()
        streamData = dict(r.get('items')[0])

        self.chat_id = streamData['liveStreamingDetails']['activeLiveChatId']
        self.next_page = None

    def _get_liveChatId(self):
        """Get all the message starting at `next_page`
        """
        params = {
            'part': 'snippet',
            'key': API_KEY,
            'liveChatId': self.chat_id,
            # 'profileImageSize': 720,
            'pageToken': self.next_page,
            'maxResults': 200
        }

        return requests.get(YT_API_CHAT_DATA_ENDPOINT,
                            headers=None, params=params).json()

    def _parse(self, frase):
        frases_lst = frase.lower().split(" ")
        return [cmd for cmd in VALID_CMD if f"{CHAR_CMD}{cmd}" in frases_lst]

    def _make_sound(self, cmd_lst):
        for cmd in cmd_lst:
            if cmd in SOUNDS_CMD:
                logger.info(f"making {cmd}")
                fn = SOUNDS_CMD.get(cmd)
                if fn:
                    wave_obj = sa.WaveObject.from_wave_file(str(fn))
                    play_obj = wave_obj.play()
                    # play_obj.wait_done()  # Wait until sound has finished playing
                else:
                    logger.warning("Comando no valido")

    def make_light(self, cmd_lst):
        if "led" in cmd_lst:
            requests.get(RASPI_HOST)

    def scan_chat(self, ignore_history):
        if ignore_history:
            logger.info("ignoring history")
            response = self._get_liveChatId()
            if response.get("error"):
                raise Exception(response)
            else:
                items = response["items"]
                self.next_page = response["nextPageToken"]
            sleep(5)

        logger.info("Starting listening")
        while True:
            response = self._get_liveChatId()
            if response.get("error"):
                raise Exception(response)
            else:
                items = response["items"]
                self.next_page = response["nextPageToken"]

            cmd_lst = []
            for item in items:
                if "liveChatId" in item['snippet']:
                    logger.info(item['snippet']['authorChannelId'])
                    logger.info(item['snippet']['displayMessage'])
                    cmd = self._parse(item['snippet']['displayMessage'])
                    if len(cmd) > 0:
                        cmd_lst.append(cmd[0])
                else:
                    pass
            if len(cmd_lst) > 0:
                self._make_sound(cmd_lst)
                self.make_light(cmd_lst)
            sleep(5)


if __name__ == "__main__":
    scanner = live_chat()
    scanner.scan_chat(True)
