import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

def create_daily_df(df):
  daily_sharing_df = df.resample(rule='D', on='dteday').agg({"casual": "sum", "registered": "sum", "cnt": "sum"})
  daily_sharing_df.index = daily_sharing_df.index.strftime('%Y-%m-%d')
  daily_sharing_df = daily_sharing_df.reset_index()
  daily_sharing_df.rename(columns={"casual": "casual_sharing", "registered": "registered_sharing", "cnt": "total_sharing"}, inplace=True)
  return daily_sharing_df

def create_weekly_df(df):
  weekly_sharing_df = df.resample(rule='W', on='dteday').agg({"casual": "sum", "registered": "sum", "cnt": "sum"})
  weekly_sharing_df.index = weekly_sharing_df.index.strftime('%U-%Y')
  weekly_sharing_df = weekly_sharing_df.reset_index()
  weekly_sharing_df.rename(columns={"casual": "casual_sharing", "registered": "registered_sharing", "cnt": "total_sharing"}, inplace=True)
  return weekly_sharing_df

def create_monthly_df(df):
  monthly_sharing_df = df.resample(rule='M', on='dteday').agg({"casual": "sum", "registered": "sum", "cnt": "sum"})
  monthly_sharing_df.index = monthly_sharing_df.index.strftime('%B-%Y')
  monthly_sharing_df = monthly_sharing_df.reset_index()
  monthly_sharing_df.rename(columns={"casual": "casual_sharing", "registered": "registered_sharing", "cnt": "total_sharing"}, inplace=True)
  return monthly_sharing_df

def create_holiday_df(df):
  holiday_sharing_df = df.groupby(by=["holiday"], sort=False).agg({"cnt": "sum"})
  return holiday_sharing_df

def create_workingday_df(df):
  workingday_sharing_df = df.groupby(by=["workingday"], sort=False).agg({"cnt": "sum"})
  return workingday_sharing_df

def create_weather_df(df):
  weather_sharing_df = df.groupby(by=["weathersit"], sort=False).agg({"cnt": "sum"})
  return weather_sharing_df

def create_season_df(df):
  season_sharing_df = df.groupby(by=["season"], sort=False).agg({"cnt": "sum"})
  return season_sharing_df

day_hour_df = pd.read_csv("/content/proyekdicoding/day_hour_data.csv")

datetime_columns = ["dteday"]
day_hour_df.sort_values(by="dteday", inplace=True)
day_hour_df.reset_index(inplace=True)
 
for column in datetime_columns:
    day_hour_df[column] = pd.to_datetime(day_hour_df[column])

min_date = day_hour_df["dteday"].min()
max_date = day_hour_df["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Time Range',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_hour_df[(day_hour_df["dteday"] >= str(start_date)) & (day_hour_df["dteday"] <= str(end_date))]

daily_sharing_df = create_daily_df(main_df)
weekly_sharing_df = create_weekly_df(main_df)
monthly_sharing_df = create_monthly_df(main_df)
holiday_sharing_df = create_holiday_df(main_df)
workingday_sharing_df = create_workingday_df(main_df)
season_sharing_df = create_season_df(main_df)
weather_sharing_df = create_weather_df(main_df)

st.header('Bike Sharing Dashboard :sparkles:')

st.subheader('Daily Bike Sharing')

col1, col2 = st.columns(2)

with col1:
  casual_sharing = daily_sharing_df.casual_sharing.sum()
  st.metric("Casual sharing", value=casual_sharing)
  registered_sharing = daily_sharing_df.registered_sharing.sum()
  st.metric("Registered sharing", value=registered_sharing)

with col2:
  total_sharing = daily_sharing_df.total_sharing.sum()
  st.metric("Total sharing", value=total_sharing)

col3, col4 = st.columns(2)
 
with col3:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
      daily_sharing_df["dteday"],
      daily_sharing_df["casual_sharing"],
      marker='o', 
      linewidth=2,
      color="#90CAF9"
      )
    plt.xticks(fontsize=10,rotation=90)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.tick_params(axis='x', labelsize=15)
    plt.title("Daily Casual Bike Sharing", loc="center", fontsize=15)
    
    st.pyplot(fig)
 
with col4:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
      daily_sharing_df["dteday"],
      daily_sharing_df["registered_sharing"],
      marker='o', 
      linewidth=2,
      color="#90CAF9"
      )
    plt.xticks(fontsize=10,rotation=90)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.tick_params(axis='x', labelsize=15)
    plt.title("Daily Registered Bike Sharing", loc="center", fontsize=15)
    
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    daily_sharing_df["dteday"],
    daily_sharing_df["total_sharing"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
plt.xticks(fontsize=10,rotation=90)
plt.yticks(fontsize=10)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.title("Daily Total Bike Sharing", loc="center", fontsize=15)
 
st.pyplot(fig)

st.subheader('Weekly Bike Sharing')

col1, col2 = st.columns(2)

with col1:
  casual_sharing = weekly_sharing_df.casual_sharing.sum()
  st.metric("Casual sharing", value=casual_sharing)
  registered_sharing = weekly_sharing_df.registered_sharing.sum()
  st.metric("Registered sharing", value=registered_sharing)

with col2:
  total_sharing = weekly_sharing_df.total_sharing.sum()
  st.metric("Total sharing", value=total_sharing)

col3, col4 = st.columns(2)
 
with col3:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
      weekly_sharing_df["dteday"],
      weekly_sharing_df["casual_sharing"],
      marker='o', 
      linewidth=2,
      color="#90CAF9"
      )
    plt.xticks(fontsize=10,rotation=90)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.tick_params(axis='x', labelsize=15)
    plt.title("Weekly Casual Bike Sharing", loc="center", fontsize=15)
    
    st.pyplot(fig)
 
with col4:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
      weekly_sharing_df["dteday"],
      weekly_sharing_df["registered_sharing"],
      marker='o', 
      linewidth=2,
      color="#90CAF9"
      )
    plt.xticks(fontsize=10,rotation=90)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.tick_params(axis='x', labelsize=15)
    plt.title("Weekly Registered Bike Sharing", loc="center", fontsize=15)
    
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    weekly_sharing_df["dteday"],
    weekly_sharing_df["total_sharing"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
plt.xticks(fontsize=10,rotation=90)
plt.yticks(fontsize=10)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.title("Weekly Total Bike Sharing", loc="center", fontsize=15)
 
st.pyplot(fig)

st.subheader('Monthly Bike Sharing')

col1, col2 = st.columns(2)

with col1:
  casual_sharing = monthly_sharing_df.casual_sharing.sum()
  st.metric("Casual sharing", value=casual_sharing)
  registered_sharing = monthly_sharing_df.registered_sharing.sum()
  st.metric("Registered sharing", value=registered_sharing)

with col2:
  total_sharing = monthly_sharing_df.total_sharing.sum()
  st.metric("Total sharing", value=total_sharing)

col3, col4 = st.columns(2)
 
with col3:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
      monthly_sharing_df["dteday"],
      monthly_sharing_df["casual_sharing"],
      marker='o', 
      linewidth=2,
      color="#90CAF9"
      )
    plt.xticks(fontsize=10,rotation=90)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.tick_params(axis='x', labelsize=15)
    plt.title("Monthly Casual Bike Sharing", loc="center", fontsize=15)
    
    st.pyplot(fig)
 
with col4:
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.plot(
      monthly_sharing_df["dteday"],
      monthly_sharing_df["registered_sharing"],
      marker='o', 
      linewidth=2,
      color="#90CAF9"
      )
    plt.xticks(fontsize=10,rotation=90)
    plt.yticks(fontsize=10)
    plt.tick_params(axis='y', labelsize=15)
    plt.tick_params(axis='x', labelsize=15)
    plt.title("Monthly Registered Bike Sharing", loc="center", fontsize=15)
    
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_sharing_df["dteday"],
    monthly_sharing_df["total_sharing"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
plt.xticks(fontsize=10,rotation=90)
plt.yticks(fontsize=10)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.title("Monthly Total Bike Sharing", loc="center", fontsize=15)
 
st.pyplot(fig)

st.subheader('Comparison Casual and Registered Bike Sharing')

new_daily_sharing_df = daily_sharing_df.drop(columns=["dteday", "total_sharing"])
new_daily_sharing_df = new_daily_sharing_df.transpose()
new_daily_sharing_df["total"] = new_daily_sharing_df.sum(axis=1)

fig_1, ax_1 = plt.subplots(figsize=(16, 8))
ax_1.pie(new_daily_sharing_df["total"], labels=["casual", "registered"], autopct="%1.0f%%")
plt.title("Comparison Casual and Registered Bike Sharing", loc="center", fontsize=15)

st.pyplot(fig_1)

st.subheader('Bike Sharing by Holiday or Not Holiday')

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig = plt.figure(figsize=(16, 8))
sns.barplot(
    y="cnt",
    x="holiday",
    data=holiday_sharing_df.sort_values(by="cnt", ascending=False),
    palette=colors
)
plt.title("Number of Bike Sharing by Holiday or Not Holiday", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Workingday or Not Workingday')

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig = plt.figure(figsize=(16, 8))
sns.barplot(
    y="cnt",
    x="workingday",
    data=workingday_sharing_df.sort_values(by="cnt", ascending=False),
    palette=colors
)
plt.title("Number of Bike Sharing by Workingday or Not Holiday", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Weather')

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig = plt.figure(figsize=(16, 8))
sns.barplot(
    y="cnt",
    x="weathersit",
    data=weather_sharing_df.sort_values(by="cnt", ascending=False),
    palette=colors
)
plt.title("Number of Bike Sharing by Weather", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Season')

fig = plt.figure(figsize=(16, 8))
sns.barplot(
    y="cnt",
    x="season",
    data=season_sharing_df.sort_values(by="cnt", ascending=False),
    palette=colors
)
plt.title("Number of Bike Sharing by Season", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=15)
plt.tick_params(axis='x', labelsize=15)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Year')

yr_df = day_hour_df.groupby(by=["yr"], sort=False).agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
})

colors = ["#D3D3D3", "#72BCD4"]

fig = plt.figure(figsize=(10, 5))
sns.barplot(
    y="cnt",
    x="yr",
    data=yr_df,
    palette=colors
)
plt.title("Number of Bike Sharing by Year", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Month')

mnth_df = day_hour_df.groupby(by=["mnth"], sort=False).agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
})

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig = plt.figure(figsize=(10, 5))
sns.barplot(
    y="cnt",
    x="mnth",
    data=mnth_df,
    palette=colors
)
plt.title("Number of Bike Sharing by Month", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Weekday')

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekday_df = day_hour_df.groupby(by=["weekday"], sort=False).agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
}).reindex(days)

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3"]

fig = plt.figure(figsize=(10, 5))
sns.barplot(
    y="cnt",
    x="weekday",
    data=weekday_df,
    palette=colors
)
plt.title("Number of Bike Sharing by Weekday", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader('Bike Sharing by Hour')

hr_df = day_hour_df.groupby(by=["hr"], sort=False).agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
})

colors = ["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

fig = plt.figure(figsize=(10, 5))
sns.barplot(
    y="cnt",
    x="hr",
    data=hr_df.sort_values(by="cnt", ascending=False),
    palette=colors
)
plt.title("Number of Bike Sharing by Hour", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='x', labelsize=12)
plt.xticks(rotation=45)

st.pyplot(fig)
