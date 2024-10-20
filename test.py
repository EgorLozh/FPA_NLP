import os
import wave
import json
from vosk import Model, KaldiRecognizer
from pydub import AudioSegment

# Преобразуем аудиофайл в нужный формат (моно, 16-bit PCM, 16000 Hz)
audio = AudioSegment.from_wav("data/вова.wav")
audio = audio.set_channels(1)  # моно
audio = audio.set_frame_rate(16000)  # частота дискретизации 16000 Hz
audio = audio.set_sample_width(2)  # 16-битный PCM

# Сохраняем преобразованный файл
audio.export("data/processed_audio.wav", format="wav")

# Загружаем модель
model = Model("models/vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 16000)

# Открываем обработанный аудиофайл
wf = wave.open("data/processed_audio.wav", "rb")

# Проверяем, что аудиофайл соответствует требованиям
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
    print("Audio file must be WAV format mono PCM.")
    exit(1)

# Обрабатываем аудиофайл
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        print(result)
    else:
        print(rec.PartialResult())

# Финальный результат
print(rec.FinalResult())
