from pyannote.audio import Audio
from pyannote.core import Segment
from pyannote.audio.pipelines.speaker_verification import PretrainedSpeakerEmbedding
import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

embedding_model = PretrainedSpeakerEmbedding( 
    "speechbrain/spkrec-ecapa-voxceleb",
    device=torch.device(DEVICE)
)

def segment_embedding(segment, path, duration):
    audio = Audio()
    start = segment["start"]
    end = min(duration, segment["end"])
    clip = Segment(start, end)
    waveform, _ = audio.crop(path, clip)
    return embedding_model(waveform[None])
