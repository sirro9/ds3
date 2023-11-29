import streamlit as st
import pandas as pd

st.title("About Data ❄️")
st.write(
    "The dataset used for Customer Personality Analysis is sourced from Kaggle, and it contains 2240 rows and 29 features.")

st.write("## Features for Analysis")
st.write(
    "The features are divided to different aspect:")

# st.markdown("- **Education:** This variable represents the education level of the customers.")
# st.markdown("- **Income:** The income of the customers is another key feature identified.")
attributes_data = {
        "People": ["ID", "Year_Birth", "Education", "Marital_Status", "Income", "Kidhome", "Teenhome", "Dt_Customer", "Recency", "Complain"],
        "Products": ["MntWines", "MntFruits", "MntMeatProducts", "MntFishProducts", "MntSweetProducts", "MntGoldProds"],
        "Promotion": ["NumDealsPurchases", "AcceptedCmp1", "AcceptedCmp2", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "Response"],
        "Place": ["NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", "NumWebVisitsMonth"]
    }

attributes_df = pd.DataFrame.from_dict(attributes_data, orient="index")
attributes_df = attributes_df.transpose()
attributes_df = attributes_df.replace(pd.NA, "")


st.table(attributes_df)

st.write(
    "These features, comprising both categorical and numerical variables, are expected to play a significant role in our clustering analysis. They can reveal meaningful connections and similarities among customers.")


st.write("## Data Link")
st.write("https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis/data")
