import os
import json

from dulwich.objects import cls
from googleapiclient.channel import Channel
from googleapiclient.discovery import build
from dotenv import load_dotenv

from helper.youtube_api_manual import channel


class Channel:
    """Класс для ютуб-канала"""
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    api_key: str = os.getenv('YT_API_KEY')
    # специальный объект для работы с API
    youtube = build('youtube', 'v3', developerKey=Channel.api_key)



    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
