from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator
from pytube import YouTube
from loguru import logger


class YoutubeTranscriptDownloader:
    def __init__(self, video_link):

        video_id = YouTube(video_link).video_id
        self.video_transcript = YouTubeTranscriptApi.get_transcript(video_id)


    def video_to_transcript(self):

        transcript = [i['text'] for i in self.video_transcript]
        return transcript


    def transcript_to_farsi(self):

        transcript = self.video_to_transcript()

        # Use any translator you like, in this example GoogleTranslator
        translated_obj = GoogleTranslator(source='auto', target='fa')
        en_fa_transcript = [(text, translated_obj.translate(text)) for text in transcript]
        return en_fa_transcript

