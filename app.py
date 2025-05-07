import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned data
df = pd.read_csv("covid_cleaned_data.csv")

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")
st.title("🦠 COVID-19 Tracker: India & Kenya")

# Convert 'date' column to datetime (if not already)
df['date'] = pd.to_datetime(df['date'])

# Convert the min and max date values to datetime objects
min_date = df['date'].min().to_pydatetime()
max_date = df['date'].max().to_pydatetime()

# Sidebar filters
with st.sidebar:
    st.header("📌 Filter Data")
    country = st.selectbox("Select a Country", df['location'].unique())
    date_range = st.slider("Select Date Range",
                           min_value=min_date,
                           max_value=max_date,
                           value=(min_date, max_date))

# Filter data based on selected country and date range
filtered_df = df[(df['location'] == country) &
                 (df['date'] >= date_range[0]) &
                 (df['date'] <= date_range[1])]

# Show the daily new cases chart
st.subheader(f"📊 Daily New Cases in {country}")
st.line_chart(filtered_df.set_index('date')['new_cases'])

# Bonus: Show daily new deaths chart
st.subheader(f"🪦 Daily New Deaths in {country}")
st.line_chart(filtered_df.set_index('date')['new_deaths'])

# Optional: Show raw data in a table if selected
if st.checkbox("Show raw data"):
    st.write(filtered_df)
