import numpy as np
from functions.transcript import transcript
from functions.get_duration import get_duration
from functions.segment_embedding import segment_embedding
from functions.clustering import clustering
from functions.transcript_to_txt import transcript_to_txt

NUM_SPEAKERS = 2

def main(path):
  path, segments = transcript(path)
  duration = get_duration(path)

  embeddings = np.zeros(shape=(len(segments), 192))
  for i, segment in enumerate(segments):
    embeddings[i] = segment_embedding(segment, path, duration)
  embeddings = np.nan_to_num(embeddings)

  segments = clustering(NUM_SPEAKERS, embeddings, segments)
  text_path = transcript_to_txt(segments)
  
  return segments

main("bot.wav")