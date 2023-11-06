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
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="YourAppName/1.0 (jeffryzhang501@gmail.com)"
)
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

# Unique Words in the Text:Unique Words in the Text:
with open("barcelona_text.py", "r") as file:
    another_text = file.read()
words_realmadrid = filtered_text.split()
words_another = another_text.split()
unique_words_realmadrid = set(words_realmadrid) - set(words_another)
for word in unique_words_realmadrid:
    print(word)
