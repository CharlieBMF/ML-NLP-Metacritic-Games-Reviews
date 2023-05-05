from data_loader import data
import seaborn as sns
import matplotlib.pyplot as plt
import string
#import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline


def text_filter(text):
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


def categorise_positive_negative(rating):
    if rating == 0 or rating == 1 or rating == 2:
        return 'negative'
    elif rating == 8 or rating == 9 or rating == 10:
        return 'positive'


data_filtered = data[(data['rating'] == 0) | (data['rating'] == 1) | (data['rating'] == 2)|
                     (data['rating'] == 8) | (data['rating'] == 9) | (data['rating'] == 10)]

print(data_filtered.describe())
print(data_filtered.info())
print(data_filtered.groupby('rating').describe())

data_filtered['length'] = data_filtered['text'].apply(len)
data_filtered['type'] = data_filtered['rating'].apply(categorise_positive_negative)

print(data_filtered)
print(data_filtered.describe())

# sns.histplot(data=data_filtered, x='length')
#
# plt.xlim(0, 4000)
# plt.show()
#
# data.hist(column='length', by='rating', bins=50)
# plt.show()


bow_transformer = CountVectorizer().fit(data_filtered['text'])
print(len(bow_transformer.vocabulary_))

#all text
text_bow = bow_transformer.transform(data_filtered['text'])
print(text_bow.shape)



#tfidf
tfidf_transformer = TfidfTransformer().fit(text_bow)

#alltext
text_tfidf = tfidf_transformer.transform(text_bow)
print(text_tfidf.shape)


text_train, text_test, rating_train, rating_test = train_test_split(text_tfidf, data_filtered['type'], test_size=0.2)

model = MultinomialNB().fit(text_train, rating_train)

predictions = model.predict(text_test)
print(classification_report(predictions, rating_test))




#pipeline
text_train, text_test, rating_train, rating_test = train_test_split(data_filtered['text'], data_filtered['type'], test_size=0.2)
pipeline = Pipeline([
    ('bow', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
])

pipeline.fit(text_train, rating_train)
predictions = pipeline.predict(text_test)
print(classification_report(predictions, rating_test))