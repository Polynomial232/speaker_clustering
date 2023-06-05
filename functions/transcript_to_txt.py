from get_timedelta import time

def transcript_to_txt(segments, path="transcript.txt"):
  f = open(path, "w")

  for (i, segment) in enumerate(segments):
    if i == 0 or segments[i - 1]["speaker"] != segment["speaker"]:
      f.write("\n" + segment["speaker"] + ' ' + str(time(segment["start"])) + '\n')
    f.write(segment["text"][1:] + ' ')
  f.close()

  return path
