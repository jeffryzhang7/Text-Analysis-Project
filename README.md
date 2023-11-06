# Text-Analysis-Project
### 1. Project Overview
 I used Wikipedia as my source to collect texts for analysis. As a big soccer fan, and with Real Madrid being my favorite team, I selected the search results for Real Madrid CF and its rival team FC Barcelona as sources for this project. Through completing this project, I used techniqus including top 10 words, unique words, text similarity, and text clustering. I aim to have a better understanding of how those two spanish club become the most popular, successful and competitive teams globally.

 ### 2. Implementation
 The major components consist of data retrieval, text preprocessing, similarity analysis, and statistical analysis. The primary data retrieval component utilizes the MediaWiki and wikipediaapi libraries to fetch Wikipedia articles, where a design decision was made to choose between these two libraries based on user agent configuration. Text preprocessing, a crucial step, involves tokenization and removal of English stopwords to clean the text data. For the similarity analysis, cosine similarity is computed between articles using the scikit-learn library. This choice of similarity metric is common for text analysis due to its effectiveness in measuring document similarity. The resulting similarity matrix is further processed using multidimensional scaling (MDS) to visualize relationships between articles in a 2D space. In another code snippet, the major components involve text processing, including removing stopwords, and identifying unique words in comparison to another text source. A design decision here is the choice to use the set difference operation to find unique words, which simplifies the process by directly highlighting differences in vocabulary between the two text sources. Overall, the components, algorithms, and data structures work together to retrieve, process, analyze, and compare textual data from Wikipedia, allowing for insights into content similarity and key terms. These choices prioritize simplicity and effectiveness in text analysis, facilitating the extraction of meaningful information from the provided articles.

  ### 3. Results
  #### Madrid: 216Real: 210club: 95first: 74European: 51 Barcelona: 46 Champions: 46 one: 44 Spanish: 41 team: 41
  Those are the top 10 words appeared in the text. It is noticeable that the presence of words like "champions" and "one" suggests Real Madrid's numerous victories and prestigious history as a football club, underscoring its reputation as one of the world's top football clubs. Additionally, the frequent mention of "Barcelona" within the text highlights the complex and significant relationship between these two football clubs, with both cooperation and intense rivalry shaping their history in the world of football. Analyzing the most frequently occurring words in a text can provide valuable insights into the core themes and topics discussed within the content, and in this case, it sheds light on Real Madrid's achievements and its relationship with its rival, Barcelona.

  #### cosine Similarity between Barcelona and Real Madrid text: 0.7259178129544208
A cosine similarity score of 0.7259178129544208 implies that the text or vectors representing "Barcelona" and "Real Madrid" have a relatively high degree of similarity. It shows that these two clubs have a very deep and profound historical connection even until nowadays.

#### Jose Zidane Hazard Ronaldo Fernández Calderón Raúl Madrileño
These are the portion of the unique words that appeared only in the "realmadrid" text, I noticed that many of them are names of the legendary players who had a significant impact throughout the history of Real Madrid. Besides there isn't a lot of helpful information.

![text clustering](https://github.com/OIM3640/Text-Analysis-Project/assets/143424317/525d9b8c-6991-460e-a238-8306cdfacdd4)

#### 4. Reflection

In my text analysis project on Real Madrid CF and FC Barcelona, I explored the rich history and intricate relationship between two of the world's foremost football clubs. As an avid soccer fan and a devoted Real Madrid supporter, this project was a personal journey. The methodologies that I applied are helpful overall, while they are somewhat superficial, I wish that I could dig into the details more in te future. 







