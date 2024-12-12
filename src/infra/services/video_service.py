from moviepy.editor import VideoFileClip
import requests
import gdown

from src.infra.services.logger_service import LoggerService


class VideoService:
    def __init__(self):
        self.logger = LoggerService()

    def _request_download(self, url, video_path):
        response = requests.get(url, stream=True)
        self.logger.info(response.json())
        if response.status_code == 200:
            with open(video_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        else:
            self.logger.error(f"Failed to download video from {url}")

    def _google_drive_download(self, url, video_path):
        gdown.download(url, video_path, quiet=False, fuzzy=True)        
        

    def download_video(self, url: str, video_path: str):
        self.logger.info(f"Downloading video from {url} to {video_path}")
        try:
            if url.startswith("https://drive.google.com/file/d/"):
                self._google_drive_download(url, video_path)
            else:
                self._request_download(url, video_path)

            self.logger.info(f"Video downloaded to {video_path}")

        except Exception as e:
            self.logger.error(f"Error downloading video: {str(e)}")

        # TODO: add error handling
        

    def extarct_audio(self, video_path, audio_path):
        self.logger.info(f"Extracting audio from {video_path} to {audio_path}")

        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        video.close()
        audio.close()

        self.logger.info(f"Audio extracted to {audio_path}")
