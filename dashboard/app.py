import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sqlite3
import os

st.set_page_config(page_title="RidePulse Dashboard", page_icon="🚖", layout="wide")

@st.cache_data
def load_data():
    # Determine base path (works both locally and on Streamlit Cloud)
    base_paths = [".", ".."]
    
    # Try SQLite first
    for base in base_paths:
        db_path = os.path.join(base, "ridepulse.db")
        if os.path.exists(db_path):
            try:
                conn = sqlite3.connect(db_path)
                df = pd.read_sql("SELECT * FROM fact_trips LIMIT 100000", conn)
                conn.close()
                return df
            except:
                pass
    
    # Try sample CSV for Streamlit Cloud
    for base in base_paths:
        sample_path = os.path.join(base, "data", "ridepulse_sample.csv")
        if os.path.exists(sample_path):
            return pd.read_csv(sample_path)
    
    # Try full CSV
    for base in base_paths:
        csv_path = os.path.join(base, "data", "ridepulse_processed.csv")
        if os.path.exists(csv_path):
            return pd.read_csv(csv_path).head(100000)
    
    # Generate sample data if nothing exists
    st.warning("⚠️ No data found. Using sample data for demo purposes.")
    return generate_sample_data()

@st.cache_data
def load_kpi_hourly():
    # Determine base path
    base_paths = [".", ".."]
    
    # Try SQLite first
    for base in base_paths:
        db_path = os.path.join(base, "ridepulse.db")
        if os.path.exists(db_path):
            try:
                conn = sqlite3.connect(db_path)
                df = pd.read_sql("SELECT * FROM kpi_hourly", conn)
                conn.close()
                return df
            except:
                pass
    
    # Generate from CSV or sample data
    df = load_data()
    kpi = df.groupby("pickup_hour").agg({
        "total_amount": "sum",
        "fare_amount": "mean",
        "trip_distance": "mean",
        "average_speed": "mean"
    }).reset_index()
    kpi.columns = ["pickup_hour", "total_revenue", "avg_fare", "avg_distance", "avg_speed"]
    kpi["trip_count"] = df.groupby("pickup_hour").size().values
    return kpi

@st.cache_data
def load_kpi_passenger():
    # Determine base path
    base_paths = [".", ".."]
    
    # Try SQLite first
    for base in base_paths:
        db_path = os.path.join(base, "ridepulse.db")
        if os.path.exists(db_path):
            try:
                conn = sqlite3.connect(db_path)
                df = pd.read_sql("SELECT * FROM kpi_passenger", conn)
                conn.close()
                return df
            except:
                pass
    
    # Generate from CSV or sample data
    df = load_data()
    kpi = df.groupby("passenger_count").agg({
        "total_amount": "sum",
        "fare_amount": "mean"
    }).reset_index()
    kpi.columns = ["passenger_count", "total_revenue", "avg_fare"]
    kpi["trip_count"] = df.groupby("passenger_count").size().values
    return kpi

def generate_sample_data():
    """Generate sample data for demo when real data is not available"""
    import numpy as np
    np.random.seed(42)
    
    n_samples = 10000
    df = pd.DataFrame({
        "VendorID": np.random.choice([1, 2], n_samples),
        "tpep_pickup_datetime": pd.date_range("2025-01-01", periods=n_samples, freq="5min"),
        "passenger_count": np.random.choice([1, 2, 3, 4, 5], n_samples, p=[0.7, 0.15, 0.08, 0.05, 0.02]),
        "trip_distance": np.random.exponential(3, n_samples),
        "fare_amount": np.random.exponential(15, n_samples) + 5,
        "total_amount": np.random.exponential(18, n_samples) + 7,
        "pickup_hour": np.random.randint(0, 24, n_samples),
        "average_speed": np.random.normal(12, 3, n_samples).clip(5, 30)
    })
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
