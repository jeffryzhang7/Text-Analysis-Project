from mediawiki import MediaWiki
wikipedia = MediaWiki()
barcelona= wikipedia.page("FC Barcelona")
print(barcelona.title)
print(barcelona.content)
another_text= barcelona

import wikipediaapi
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent="YourAppName/1.0 (jeffryzhang501@gmail.com)"
)
barcelona_page = wiki_wiki.page("FC Barcelona")
if barcelona_page.exists():
    content = barcelona_page.text
else:
    print("Page does not exist.")
words = content.split()
stop_words = set(stopwords.words("english"))
filtered_words = [word for word in words if word.lower() not in stop_words]
filtered_text = " ".join(filtered_words)
print(filtered_text)


