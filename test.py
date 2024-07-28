import pandas as pd


df = pd.read_csv(r'C:\Users\ibrah\PycharmProjects\freelaceQAchat\Complate\result.csv')
df = df.drop("Unnamed: 0", axis=1)
df.to_csv('result.csv', index=False)