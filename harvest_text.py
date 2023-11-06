from mediawiki import MediaWiki

wikipedia = MediaWiki()
realmadrid= wikipedia.page("Real Madrid CF")
print(realmadrid.title)
print(realmadrid.content)

# Remove stop words
import wikipediaapi
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
wiki_wiki = wikipediaapi.Wikipedia('en')  # 'en' for English Wikipedia
realmadrid_page = wiki_wiki.page("Real Madrid CF")
if realmadrid_page.exists():
    content = realmadrid_page.text
else:
    print("Page does not exist.")
words = content.split()
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = " ".join(filtered_words)
print(filtered_text)
