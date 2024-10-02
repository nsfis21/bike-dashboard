import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


day_df = pd.read_csv("https://raw.githubusercontent.com/nsfis21/bike-sharing/refs/heads/main/day.csv")

season_data = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_data = {1:"Clear & Few clouds", 2:"Mist & Cloudy", 3:"Light Snow & Light Rain", 4:"Heavy Rain & Ice"}
yr_label = {0: "2011", 1: "2012"}
mnths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

day_df["name_season"] = day_df["season"].map(season_data)
day_df["name_weather"] = day_df["weathersit"].map(weather_data)
day_df["year"] = day_df["yr"].map(yr_label)

#-----------------
#Judul dashboard streamlit
st.title("Bike Sharing Data Visualization")

#Visualisasi untuk melihat hubungan musim dengan penyewa sepeda
st.markdown("## A. Number of bicycle rentals based on season")
data_season= day_df.groupby("name_season").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
}).reset_index()
fig, ax = plt.subplots(figsize=(6, 3))
sns.barplot(
    x="name_season", y="cnt", data=data_season)
ax.set_title("Count of bicycle rentals based on season", fontsize=11)
ax.set_ylabel("Count of Total Rental", fontsize=10)
ax.set_xlabel("Season", fontsize=10)
st.pyplot(fig)

#------------
#Visualisasi hubungan cuaca dengan penyewa sepeda
st.markdown("## B. Weather relationship with bicycle rental")
fig, ax = plt.subplots(figsize=(6, 3))
sns.boxplot(x="name_weather", y="cnt", data=day_df)
ax.set_xlabel("Weather")
ax.set_ylabel("Total Bike Rentals")
ax.set_title("Distribution of Bike Rentals by Weather")
ax.tick_params(rotation=45)
st.pyplot(fig)

#------------
#Visualisasi penyewa sepeda berdasarkan bulan
st.markdown("## C. Number of bicycle renters by month")
mnth_data = day_df.groupby("mnth").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
}).reset_index()
mnths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
mnth_data["mnth_name"] = mnths
fig, ax = plt.subplots(figsize=(6, 3))
sns.lineplot(x=mnth_data["mnth_name"], y=mnth_data["casual"], label="Casual", marker = "o")
sns.lineplot(x=mnth_data["mnth_name"], y=mnth_data["registered"], label="Registered", marker = "o")
sns.lineplot(x=mnth_data["mnth_name"], y=mnth_data["cnt"], label="Total", marker = "o")
ax.set_title("Count of bicycle rentals based on month", fontsize=11)
ax.set_ylabel("Count of Total Rental", fontsize=10)
ax.set_xlabel("Month", fontsize=10)
st.pyplot(fig)

#---- 
# Visualisasi trend sewa sepeda tahun 2011-2012
st.markdown("## D. Bicycle rental trends in 2011-2012 ")
day_df["year"] = day_df["yr"].map(yr_label)
data_yr = day_df.groupby("dteday").agg({
    "cnt": "sum"
}).reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
sns.lineplot(x="dteday", y="cnt", data=day_df, hue="year", palette="coolwarm")
ax.set_xlabel("Date")
ax.set_ylabel("Total Bike Rentals")
ax.set_title("Trend of Bike Rentals over Time")
ax.tick_params(rotation=45)
st.pyplot(fig)

