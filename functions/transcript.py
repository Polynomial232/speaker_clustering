import subprocess
import whisper

MODEL_SIZE = 'base'

def transcript(path):
    if path[-3:] != 'wav':
        subprocess.call(['ffmpeg', '-i', path, 'audio.wav', '-y'])
        path = 'audio.wav'

    model = whisper.load_model(MODEL_SIZE)
    result = model.transcribe(path)
    segments = result["segments"]

    return path, segments
