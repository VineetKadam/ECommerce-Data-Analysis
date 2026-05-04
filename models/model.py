import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("../data/cleaned_data.csv")

data = df[['Sales']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(data)

print(df.groupby('Cluster')['Sales'].mean())

df.to_csv("../data/clustered_data.csv", index=False)

print("Clustering done! Data saved.")