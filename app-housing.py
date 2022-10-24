import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Weihao Jiang')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Median House Price:', 0, 50001, 20000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type:',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


income_filter = st.sidebar.radio(
    'Choose income level',
     ['Low', 'Medium', 'High'])


# filter by population
df = df[df.median_house_value >= price_filter]

# filter by capital
df = df[df.ocean_proximity.isin(location_filter)]

if income_filter == 'Low':
     df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
     df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
elif income_filter == 'High':
     df = df[df.median_income > 4.5]

# show on map
st.subheader('See more filters in the sidebar:')
st.map(df)

# show dataframe
st.subheader('Histogram of the Median House Value:')
fig, ax = plt.subplots(figsize=(10, 5))
df.median_house_value.hist(bins=30)

st.pyplot(fig)