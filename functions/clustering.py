from sklearn.cluster import AgglomerativeClustering

def clustering(num_speakers, embeddings, segments):
  clustering = AgglomerativeClustering(num_speakers).fit(embeddings)
  labels = clustering.labels_
  for i in range(len(segments)):
    segments[i]["speaker"] = 'SPEAKER ' + str(labels[i] + 1)

  return segments