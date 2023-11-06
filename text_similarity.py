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

# Calculate cosine similarity
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([barcelona_text, realmadrid_text])
cosine_sim = cosine_similarity(X[0], X[1])

print("Cosine Similarity between Barcelona and Real Madrid text:", cosine_sim[0][0])
