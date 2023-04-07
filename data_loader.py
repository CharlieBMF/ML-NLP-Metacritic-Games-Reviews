import pandas as pd

data = pd.DataFrame()

for i in range(70):
    data_load = pd.read_csv('data_page'+str(i)+'.csv')
    data = data.append(data_load)
    print(f'File number {i} loaded')
data = data.reset_index()
data.drop(['Unnamed: 0', 'index'], axis=1, inplace=True)
data.dropna(inplace=True)
