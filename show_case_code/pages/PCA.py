import streamlit as st

st.title("PCA Principle: Dimensionality Reduction ❄️")

st.write("Principal Component Analysis (PCA) is a technique for mapping high-dimensional data to a lower-dimensional space with linear transformation, "
         "reducing the dimensionality of data while retaining its essential information. PCA helps us handle high-dimensional data, making it easier for "
         "analysis and visualization. ")

st.write("## How PCA Works")
image_path = "pca.png"
st.image(image_path, use_column_width=True)

st.write("## PCA Implement")
pca_code = """
from sklearn.decomposition import PCA
X = ...
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
"""

st.code(pca_code, language="python")

