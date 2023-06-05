import numpy as np
from functions.transcript import transcript, transcript_to_txt
from functions.get_duration import get_duration
from functions.segment_embedding import segment_embedding
from functions.clustering import clustering

import argparse

NUM_SPEAKERS = 2

def main(path):
    path, segments = transcript(path)
    duration = get_duration(path)

    embeddings = np.zeros(shape=(len(segments), 192))
    for i, segment in enumerate(segments):
        embeddings[i] = segment_embedding(segment, path, duration)
    embeddings = np.nan_to_num(embeddings)

    segments = clustering(NUM_SPEAKERS, embeddings, segments)
    _ = transcript_to_txt(segments)
    
    return segments

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--filename', required=True)
    args = parser.parse_args()

    main(args.filename)