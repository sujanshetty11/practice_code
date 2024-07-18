import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial.distance import euclidean, cityblock
from sklearn.metrics.pairwise import cosine_similarity

# Document set
documents = [
    "Shipment of gold damaged in a fire",
    "Delivery of silver arrived in a silver truck",
    "Shipment of gold arrived in a truck",
    "Purchased silver and gold arrived in a wooden truck",
    "The arrival of gold and silver shipment is delayed."
]

# Query sentence
query = "gold silver truck"

# Initialize CountVectorizer
vectorizer = CountVectorizer(stop_words="english")
X = vectorizer.fit_transform(documents + [query])
vectors = X.toarray()
doc_vectors, query_vector = vectors[:-1], vectors[-1]

# Compute distances and similarities
def compute_distances(doc_vectors, query_vector):
    euclidean_distances = [euclidean(doc, query_vector) for doc in doc_vectors]
    manhattan_distances = [cityblock(doc, query_vector) for doc in doc_vectors]
    cosine_similarities = cosine_similarity(doc_vectors, query_vector.reshape(1, -1)).flatten()
    return euclidean_distances, manhattan_distances, cosine_similarities

euclidean_distances, manhattan_distances, cosine_similarities = compute_distances(doc_vectors, query_vector)

# Ranking documents
top_2_euclidean = np.argsort(euclidean_distances)[:2] + 1
top_2_manhattan = np.argsort(manhattan_distances)[:2] + 1
top_2_cosine = np.argsort(-cosine_similarities)[:2] + 1

# Output results
print("Euclidean Distance:", euclidean_distances)
print("Manhattan Distance:", manhattan_distances)
print("Cosine Similarity:", cosine_similarities)
print("\nTop 2 documents using Euclidean distance:", top_2_euclidean)
print("Top 2 documents using Manhattan distance:", top_2_manhattan)
print("Top 2 documents using Cosine similarity:", top_2_cosine)
