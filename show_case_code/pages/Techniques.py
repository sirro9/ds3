import streamlit as st


st.title("Techniques ❄️")

st.write("In this analysis, several techniques will be employed to gain insights into customer personality.")

st.write("## Data Preprocessing")
st.write("The first step involves data preprocessing to handle missing or dirty data. This ensures the dataset is cleaned and ready for analysis.")

st.write("## Exploratory Data Analysis")
st.write("EDA is then performed to explore the dataset and relationships among the variables. "
         "This step provides a comprehensive understanding of the data.")

st.write("## Dimensionality Reduction")

st.write("With 29 features in the dataset, [[PCA](http://localhost:8501/PCA)] (DS II) is employed for dimensionality reduction."
         " This technique helps reduce the complexity of the dataset while retaining essential information.")

st.write("## Clustering")
st.write("Despite the presence of a response variable, clustering techniques will be applied to explore "
         "customer personality. Cluster models, including [[K-means](http://localhost:8501/K_Means)] and [[DBSCAN](http://localhost:8501/DBSCAN)] "
         "(DS III), will be used to group "
         "similar data points into clusters. This allows for uncovering patterns and segmenting the dataset into distinct groups.")

st.write("## Model Evalution")
st.write("The two clustering methods will be compared using the [[Silhouette Score](http://localhost:8501/Silhouette_Score)]. Additionally, the Elbow Method will "
         "be utilized during the clustering process to determine the optimal number of clusters.")
