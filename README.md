# ML-NLP-Metacritic-Games-Reviews
Machine Learning NLP project to webscrap metacritic.com user games reviews, train NLP model and evaluate if review is POSITIVE or NEGATIVE.

# Decription

A task to determine the impact of the commentary issued on the www.metacritic.com website in relation to the games. Comments are issued by users according to the following scheme:

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/be10f778-01c6-4ecd-bd30-3e0db9d9e1fe)

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

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/d8ef3dd0-06ae-4aa1-bfb5-1e3cacdaf97f)

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/3e2280c0-8f60-48f6-bac5-2b9e50cc5bed)

![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/28fa20c6-1ca1-4a4c-8696-364de5e1708f)

# Filtering and data analysis
  
  The following modifications were made during data analysis and filtering:
  <ul>
<li> only comments with ratings of 0,1,2 and 8,9,10 were used. as a result, the number of comments decreased to 160k, </li>
<li> added column referring to text length, </li>
<li> added column specifying positive (8,9,10 ratings) or negative (0,1,2 ratings) rating, </li>
  </ul>
  
  Data in columns:
  
![image](https://github.com/CharlieBMF/ML-NLP-Metacritic-Games-Reviews/assets/109242797/ab2393ac-cf99-4653-b5c0-e7f2862addac)
  
  
