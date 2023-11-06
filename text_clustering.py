from mediawiki import MediaWiki
import wikipediaapi
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
nltk.download('stopwords')
wikipedia = MediaWiki()

# Get content for FC Barcelona and remove stop words
barcelona = wikipedia.page("FC Barcelona")
barcelona_text = barcelona.content
words = barcelona_text.split()
stop_words = set(stopwords.words("english"))
barcelona_words = [word for word in words if word.lower() not in stop_words]
barcelona_text = " ".join(barcelona_words)

# Get content for Real Madrid CF and remove stop words
realmadrid = wikipedia.page("Real Madrid CF")
realmadrid_text = realmadrid.content
words = realmadrid_text.split()
realmadrid_words = [word for word in words if word.lower() not in stop_words]
realmadrid_text = " ".join(realmadrid_words)

# Text Clustering

import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# these are the similarities computed from the previous section
S = np.asarray([[1., 0.90850572, 0.96451312, 0.97905034, 0.78340575],
    [0.90850572, 1., 0.95769915, 0.95030073, 0.87322494],
    [0.96451312, 0.95769915, 1., 0.98230284, 0.83381607],
    [0.97905034, 0.95030073, 0.98230284, 1., 0.82953109],
    [0.78340575, 0.87322494, 0.83381607, 0.82953109, 1.]])

# dissimilarity is 1 minus similarity
dissimilarities = 1 - S

# compute the embedding
coord = MDS(dissimilarity='precomputed').fit_transform(dissimilarities)

plt.scatter(coord[:, 0], coord[:, 1])

# Label the points
for i in range(coord.shape[0]):
    plt.annotate(str(i), (coord[i, :]))
plt.show()