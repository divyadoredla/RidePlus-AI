import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3

st.set_page_config(page_title="RidePulse Dashboard", page_icon="🚖", layout="wide")

@st.cache_data
def load_data():
    conn = sqlite3.connect("ridepulse.db")
    df = pd.read_sql("SELECT * FROM fact_trips LIMIT 100000", conn)
    conn.close()
    return df

@st.cache_data
def load_kpi_hourly():
    conn = sqlite3.connect("ridepulse.db")
    df = pd.read_sql("SELECT * FROM kpi_hourly", conn)
    conn.close()
    return df

@st.cache_data
def load_kpi_passenger():
    conn = sqlite3.connect("ridepulse.db")
    df = pd.read_sql("SELECT * FROM kpi_passenger", conn)
    conn.close()
    return df

df = load_data()
kpi_hourly = load_kpi_hourly()
kpi_passenger = load_kpi_passenger()

st.title("🚖 RidePulse - NYC Taxi Analytics Dashboard")
st.markdown("Real-time insights from NYC Yellow Taxi trips (Powered by SQLite)")

# Key Metrics from KPI tables
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Trips", f"{kpi_hourly['trip_count'].sum():,.0f}")
    
with col2:
    st.metric("Total Revenue", f"${kpi_hourly['total_revenue'].sum():,.0f}")
    
with col3:
    st.metric("Avg Fare", f"${kpi_hourly['avg_fare'].mean():.2f}")
    
with col4:
    st.metric("Avg Speed", f"{kpi_hourly['avg_speed'].mean():.1f} mph")

st.divider()

# Revenue by Hour
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Revenue by Hour")
    fig1 = px.bar(kpi_hourly, x="pickup_hour", y="total_revenue",
                  labels={"pickup_hour": "Hour of Day", "total_revenue": "Revenue ($)"},
                  color="total_revenue", color_continuous_scale="Blues")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🚕 Trips by Hour")
    fig2 = px.line(kpi_hourly, x="pickup_hour", y="trip_count",
                   labels={"pickup_hour": "Hour of Day", "trip_count": "Number of Trips"},
                   markers=True)
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Passenger Distribution and Speed Analysis
col1, col2 = st.columns(2)

with col1:
    st.subheader("👥 Passenger Distribution")
    fig3 = px.pie(kpi_passenger, values="trip_count", names="passenger_count",
                  title="Distribution of Passengers per Trip")
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("⚡ Average Speed by Hour")
    fig4 = px.area(kpi_hourly, x="pickup_hour", y="avg_speed",
                   labels={"pickup_hour": "Hour of Day", "avg_speed": "Speed (mph)"})
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# Peak Hours Analysis
st.subheader("⏰ Peak Hours Analysis")
peak_data = kpi_hourly[["pickup_hour", "trip_count", "total_revenue", "avg_fare", "avg_distance"]].copy()
peak_data.columns = ["Hour", "Trips", "Revenue", "Avg Fare", "Avg Distance"]
peak_data = peak_data.sort_values("Trips", ascending=False).head(10)

st.dataframe(peak_data, use_container_width=True)

st.divider()

# Filter Section
st.subheader("🔍 Data Explorer")
col1, col2 = st.columns(2)

with col1:
    hour_filter = st.slider("Filter by Hour", 0, 23, (0, 23))
    
with col2:
    passenger_filter = st.multiselect("Filter by Passenger Count", 
                                      options=sorted(df["passenger_count"].unique()),
                                      default=sorted(df["passenger_count"].unique())[:3])

filtered_df = df[(df["pickup_hour"] >= hour_filter[0]) & 
                 (df["pickup_hour"] <= hour_filter[1]) &
                 (df["passenger_count"].isin(passenger_filter))]

st.write(f"Showing {len(filtered_df):,} trips")
st.dataframe(filtered_df.head(100), use_container_width=True)
