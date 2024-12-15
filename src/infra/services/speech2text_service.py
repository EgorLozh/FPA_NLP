import json
import pathlib
import librosa
import noisereduce as nr
import soundfile as sf
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

from configs import Settings
from src.infra.services.logger_service import LoggerService


class Speech2TextService:
    def __init__(self, model_name: str = None):
        settings = Settings()
        if model_name is None:
            model_name = settings.VOSK_MODEL_NAME

        model_dir = pathlib.Path().resolve()/"models"
        self.logger = LoggerService()

        self.model = Model(str(model_dir/model_name))

    def remove_noises(self, audio_file: str):
        y, sr = librosa.load(audio_file, sr=None)

        reduced_noise = nr.reduce_noise(y=y, sr=sr)

        sf.write(audio_file, reduced_noise, sr)


    def recognize(self, audio_file: str, format="wav") -> str:
        rec = KaldiRecognizer(self.model, 16000)

        audio = AudioSegment.from_file(audio_file, format=format)
        audio = audio.set_channels(1)  # моно
        audio = audio.set_frame_rate(16000)  # частота дискретизации 16000 Hz
        audio_data = audio.raw_data  # Извлекаем PCM-данные

        results = []
        self.logger.info("Recognizing audio...")

        step = 4000
        for i in range(0, len(audio_data), step):
            chunk = audio_data[i:i + step]
            if rec.AcceptWaveform(chunk):
                results.append(json.loads(rec.Result())['text'])

        final_result = json.loads(rec.FinalResult())['text']
        results.append(final_result)
        self.logger.info("Audio recognized")
        
        full_text = '\n'.join([res for res in results if res])
        self.logger.info(f"Full text: {full_text}")
        return full_text
