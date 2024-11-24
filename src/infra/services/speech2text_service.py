import json
import pathlib
import wave
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

from src.infra.services.logger_service import LoggerService


class Speech2TextService:
    def __init__(self, model_name="vosk-model-small-ru-0.22"):
        model_dir = pathlib.Path().resolve()/"models"
        self.logger = LoggerService()

        self.model = Model(str(model_dir/model_name))

    def recognize(self, audio_file, format="mp3"):
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
        return full_text
