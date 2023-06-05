import subprocess
import whisper
from .get_timedelta import time

MODEL_SIZE = 'base'

def transcript(path):
    if path[-3:] != 'wav':
        subprocess.call(['ffmpeg', '-i', path, 'audio.wav', '-y'])
        path = 'audio.wav'

    model = whisper.load_model(MODEL_SIZE)
    result = model.transcribe(path)
    segments = result["segments"]

    return path, segments


def transcript_to_txt(segments, path="transcript.txt"):
  f = open(path, "w")

  for (i, segment) in enumerate(segments):
    if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
      f.write("\n" + segment["speaker"] + ' ' + str(time(segment["start"])) + '\n')
    f.write(segment["text"][1:] + ' ')
  f.close()

  return path

