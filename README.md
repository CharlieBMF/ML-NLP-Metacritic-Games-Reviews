# ML-NLP-Metacritic-Games-Reviews
Machine Learning NLP project to webscrap metacritic.com user games reviews, train NLP model and evaluate if review is POSITIVE or NEGATIVE.

# Decription

A task to determine the impact of the commentary issued on the www.metacritic.com website in relation to the games. Comments are issued by users according to the following scheme:

<div align="center" >
  
![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/be10f778-01c6-4ecd-bd30-3e0db9d9e1fe)

  </div>
<ul>
  <li>score: is determined on a scale of 0 to 10</li>
  <li>content: the user review content determining the score</li>
</ul>

<b>Data was collected from 69 pages only for PC games. About 211k comments was collected.
The aim is to train the nlp model using ml to estimate whether the content of a comment is positive (scores as 8, 9 and 10) or negative (scores as 0, 1, 2). </b>

# Steps

<h3> Scrapping </h3>

The first step was to collect data to train the model. for this purpose, a script was created to scrape the page and collect comments for all PC games. Libraries <b> selenium, Beatiful Soup and langdetect were used for this purpose </b> The script appropriately changes subsequent pages and also moves through user comments.
<br> As an additional option, it was also determined whether the comment was written in English. Comment in diffrent languages were skipped. <br>
<b> As a result, a csv file consisting of 211k comments with the corresponding ratings was obtained </b>

<div align="center" >

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/d8ef3dd0-06ae-4aa1-bfb5-1e3cacdaf97f)

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/3e2280c0-8f60-48f6-bac5-2b9e50cc5bed)

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/28fa20c6-1ca1-4a4c-8696-364de5e1708f)

  </div>
  
# Filtering and data analysis
  
  The following modifications were made during data analysis and filtering:
  <ul>
<li> only comments with ratings of 0,1,2 and 8,9,10 were used. as a result, the number of comments decreased to 160k, </li>
<li> added column referring to text length, </li>
<li> added column specifying positive (8,9,10 ratings) or negative (0,1,2 ratings) rating, </li>
  </ul>
  
  Data in columns:
  
  <div align="center" >
  
![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/ab2393ac-cf99-4653-b5c0-e7f2862addac)
  
![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/d9f0b05d-7eb3-48d9-97d4-ffef4173d956)

  
  </div>
  
Taking into account the length of the text for a given rating:

<div align="center" >
  
![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/ed8eb6de-48cf-47e7-b9d6-d8d6c78d8730)

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/3e42e492-971a-40d9-bdc6-7d6d0465bbbc)
  
![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/e655b022-94bf-4fca-84a6-8f0093dfc8e2)

  
</div>

# NLP

The set was divided into a test set with a factor of 0.2. As a result, the bow transformer was ~110k words.
Pipeline is defined as follows

Some basic Git commands are:
```python
pipeline = Pipeline([
    ('bow', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])
```
As a result, the following results were obtained:

<div align="center" >

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/446d1018-19a7-4084-af49-8a3c6d0a0db5)
  
</div>



