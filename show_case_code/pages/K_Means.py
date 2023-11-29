import streamlit as st

st.title("K-Means Clustering Principle ❄️")

st.write("K-Means is a density-based clustering algorithm that partitions data points into K clusters based on similarity. It is widely used in various applications, including customer segmentation, image compression, and anomaly detection.")

st.write("## How K-Means Works")
image_path = "KMeans.png"
st.image(image_path, use_column_width=True)
st.write("## Determine K Value")
st.write("The Elbow Method is commonly used to determine the optimal value of K. It involves running K-Means with different values of K and plotting the cost (inertia) for each K. The 'elbow' of the plot, where the cost starts to decrease at a slower rate, is considered the optimal K value.")
st.write("## Implement")
kmeans_code = """
from sklearn.cluster import KMeans
X = ...
k = ...
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)
"""

st.code(kmeans_code, language="python")
