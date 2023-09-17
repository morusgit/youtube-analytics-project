from src.channel import Channel


class Video(Channel):
    """
    Класс для видео с ютуб-канала.
    Наследуется от класса ютуб-канала.
    """

    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализирует id видео. Дальше все данные будут подтягиваться по API."""
        self.id_video = video_id
        try:
            self.video_response = self.get_service().videos().list(part='snippet,'
                                                                        'statistics,'
                                                                        'contentDetails,'
                                                                        'topicDetails',
                                                                   id=video_id
                                                                   ).execute()
            self.title: str = self.video_response['items'][0]['snippet']['title']
            self.url: str = f"https://www.youtube.com/watch?v={video_id}"
            self.view_count: int = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = self.video_response['items'][0]['statistics']['likeCount']
        except(IndexError, KeyError):
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        return self.title


class PLVideo(Video):

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Экземпляр инициализирует 'id видео' из родительского класса и 'id плейлиста'"""
        super().__init__(video_id)
        self.playlist_id = playlist_id