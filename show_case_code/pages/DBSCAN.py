import streamlit as st
st.title("DBSCAN Clustering Principle ❄️")

st.write("DBSCAN is a density-based clustering algorithm that can identify clusters of arbitrary shapes. It is particularly effective in identifying clusters in data with varying densities. DBSCAN classifies data points into three categories: core points, border points, and noise points.")
st.write("Compared to the traditional K-Means algorithm, the most significant difference with DBSCAN is that it does not require inputting the number of clusters (k). It can discover clusters of arbitrary shapes.")
st.write("## How DBSCAN Works")
image_path = "DBSCAN.png"
st.image(image_path, use_column_width=True)

st.write("## Implement")
dbscan_code = """
from sklearn.cluster import DBSCAN
X = ...
dbscan = DBSCAN(eps=0.8, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)
"""

st.code(dbscan_code, language="python")

