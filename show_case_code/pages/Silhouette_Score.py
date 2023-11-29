import streamlit as st
st.title("Silhouette Score in Clustering ❄️")

st.write("The Silhouette Score is a metric used to calculate the goodness of a clustering technique, such as K-Means. "
         "It measures how well-separated clusters are. The score ranges from -1 to 1, where a high score indicates well-defined clusters, a score around 0 indicates overlapping clusters, and a negative score suggests data points assigned to the wrong clusters.")

st.write("For every data point, the Silhouette Score takes into account the following factors:")
st.write("- **a:** The average distance from a data point to other points within the same cluster (closeness)")
st.write("- **b:** The average distance from a data point to the nearest points in a different cluster (separation).")
st.write("Specifically, the Silhouette Score is computed as: ")
formula = r"\frac{{b - a}}{{\max(a, b)}}"
st.latex(formula)