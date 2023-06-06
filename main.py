# Import the required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary(df):
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header(df):
    st.header('Header of Dataframe')
    st.write(df.head())

def display_matplotlib_scatter(df):
    st.header('Matplotlib Scatter')

    # Get the column names from the DataFrame
    columns = df.columns.tolist()

    # Select x-axis and y-axis variables using dropdowns
    x_axis = st.selectbox('Select x-axis variable:', columns)
    y_axis = st.selectbox('Select y-axis variable:', columns)

    # Generate scatter plot using Matplotlib
    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df[x_axis], y=df[y_axis])
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)

def display_plotly_scatter(df):
    st.header('Plotly Scatter')

    # Get the column names from the DataFrame
    columns = df.columns.tolist()

    # Select x-axis and y-axis variables using dropdowns
    x_axis = st.selectbox('Select x-axis variable:', columns)
    y_axis = st.selectbox('Select y-axis variable:', columns)

    # Generate scatter plot using Plotly Express
    fig = px.scatter(df, x=x_axis, y=y_axis)
    st.plotly_chart(fig)

# Add a title and intro text
st.title('Earthquake Data Explorer 🌍')
st.text('This is a web app to allow exploration of Earthquake Data')

# Sidebar setup
st.sidebar.title('📚 Sidebar')
upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
#Sidebar navigation
st.sidebar.title('🔍 Navigation')
options = st.sidebar.radio('Select what you want to display:', ['🏠 Home', '📊 Data Summary', '🗒️ Data Header', '📈 Matplotlib Scatter', '📈 Plotly Scatter'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == '🏠 Home':
    home(upload_file)
elif options == '📊 Data Summary':
    data_summary(df)
elif options == '🗒️ Data Header':
    data_header(df)
elif options == '📈 Matplotlib Scatter':
    display_matplotlib_scatter(df)
elif options == '📈 Plotly Scatter':
    display_plotly_scatter(df)
