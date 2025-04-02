import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('Diwali Sales Data.csv', encoding='unicode_escape')

# Data Cleaning
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')

# Title
st.title("Diwali Sales Analysis")

# Sidebar Options
st.sidebar.header("Filters")
selected_chart = st.sidebar.selectbox("Choose Chart Type", ["Gender", "Age Group", "State", "Marital Status", "Occupation", "Product Category"])

# Function to plot charts
def plot_chart(selected_chart):
    fig, ax = plt.subplots(figsize=(10, 5))

    if selected_chart == "Gender":
        sns.countplot(x='Gender', data=df, ax=ax)
        ax.set_title("Count of Buyers by Gender")

    elif selected_chart == "Age Group":
        sns.countplot(x='Age Group', hue='Gender', data=df, ax=ax)
        ax.set_title("Buyers by Age Group and Gender")

    elif selected_chart == "State":
        sales_state = df.groupby('State')['Orders'].sum().nlargest(10).reset_index()
        sns.barplot(x='State', y='Orders', data=sales_state, ax=ax)
        ax.set_title("Top 10 States by Orders")

    elif selected_chart == "Marital Status":
        sns.countplot(x='Marital_Status', hue='Gender', data=df, ax=ax)
        ax.set_title("Marital Status Distribution")

    elif selected_chart == "Occupation":
        sales_occ = df.groupby('Occupation')['Amount'].sum().nlargest(10).reset_index()
        sns.barplot(x='Occupation', y='Amount', data=sales_occ, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_title("Top 10 Occupations by Amount Spent")

    elif selected_chart == "Product Category":
        sales_prod = df.groupby('Product_Category')['Amount'].sum().nlargest(10).reset_index()
        sns.barplot(x='Product_Category', y='Amount', data=sales_prod, ax=ax)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
        ax.set_title("Top 10 Product Categories by Sales")

    st.pyplot(fig)

# Display selected chart
plot_chart(selected_chart)




