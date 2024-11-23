from moviepy.editor import VideoFileClip
import requests

from src.infra.services.logger_service import LoggerService


class VideoService:
    def __init__(self):
        self.logger = LoggerService()

    def download_video(self, url, video_path):
        self.logger.info(f"Downloading video from {url} to {video_path}")
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(video_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            self.logger.info(f"Video downloaded to {video_path}")
        else:
            self.logger.error(f"Failed to download video from {url}")
        # TODO: add error handling
        

    def extarct_audio(self, video_path, audio_path):
        self.logger.info(f"Extracting audio from {video_path} to {audio_path}")

        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        video.close()
        audio.close()

        self.logger.info(f"Audio extracted to {audio_path}")
