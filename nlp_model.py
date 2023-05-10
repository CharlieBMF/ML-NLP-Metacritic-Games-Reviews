import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from nltk.corpus import stopwords
from data_analysis import data_filtered


def text_filter(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


# CountVectorizer
bow_transformer = CountVectorizer().fit(data_filtered['text'])
print(f'Bow has: {len(bow_transformer.vocabulary_)} words')

# All text
text_bow = bow_transformer.transform(data_filtered['text'])

# Tfidf
tfidf_transformer = TfidfTransformer().fit(text_bow)

# All text
text_tfidf = tfidf_transformer.transform(text_bow)

# Train/Test Split
text_train, text_test, rating_train, rating_test = train_test_split(text_tfidf, data_filtered['type'],
                                                                    test_size=0.2, random_state=101)

# Model
model = MultinomialNB().fit(text_train, rating_train)


predictions = model.predict(text_test)
print(classification_report(predictions, rating_test))

# Pipeline
text_train, text_test, rating_train, rating_test = train_test_split(data_filtered['text'], data_filtered['type'],
                                                                    test_size=0.2, random_state=101)
pipeline = Pipeline([
    ('bow', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(text_train, rating_train)
predictions = pipeline.predict(text_test)
print(classification_report(predictions, rating_test))
