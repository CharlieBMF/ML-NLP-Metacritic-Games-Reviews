from data_loader import data
import seaborn as sns
import matplotlib.pyplot as plt


def categorise_positive_negative(rating):
    if rating in range(0, 3):
        return 'negative'
    elif rating in range(8, 11):
        return 'positive'


data_filtered = data[(data['rating'] == 0) | (data['rating'] == 1) | (data['rating'] == 2) |
                     (data['rating'] == 8) | (data['rating'] == 9) | (data['rating'] == 10)]
data_filtered['length'] = data_filtered['text'].apply(len)
data_filtered['type'] = data_filtered['rating'].apply(categorise_positive_negative)

print(data_filtered)
print(data_filtered.describe())
print(data_filtered.info())
print(data_filtered.groupby('rating').describe())

sns.histplot(data=data_filtered, x='length')

plt.xlim(0, 4000)
plt.show()
data_filtered.hist(column='length', by='rating', bins=50)
plt.show()