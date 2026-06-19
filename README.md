# 🚖 RidePulse - Real-Time Ride Analytics Platform

A production-grade data engineering project that simulates real-time analytics for ride-sharing platforms using NYC Yellow Taxi Trip data.

🚀 **Live Demo**: [https://rideplus-ai.streamlit.app/](https://rideplus-ai.streamlit.app/)

## 📊 Project Overview

RidePulse demonstrates end-to-end data engineering skills including data cleaning, feature engineering, streaming simulation, SQL database integration, and interactive visualization.

**🌐 Live Dashboard**: [https://rideplus-ai.streamlit.app/](https://rideplus-ai.streamlit.app/)  
**📁 GitHub Repository**: [https://github.com/divyadoredla/RidePlus-AI](https://github.com/divyadoredla/RidePlus-AI)

## ✨ Features

- **Data Pipeline**: Automated ETL for 2.8M+ trip records
- **Real-time Streaming**: Event-based trip simulation
- **SQL Database**: SQLite integration with fact and KPI tables
- **Interactive Dashboard**: Streamlit-powered analytics visualization
- **Analytics Engine**: Revenue, peak hours, and distribution analysis
- **Logging & Config**: Production-ready code structure

## 🏗️ Architecture

```
NYC Taxi Dataset
      ↓
Data Cleaning & Feature Engineering
      ↓
SQLite Database (fact_trips + KPIs)
      ↓
Streamlit Dashboard + Analytics
```

## 📁 Project Structure

```
RidePulse/
│
├── data/                          # Data files
│   ├── cleaned_data.csv
│   └── ridepulse_processed.csv
│
├── src/                           # ETL scripts
│   ├── data_cleaning.py
│   ├── eda.py
│   └── feature_engineering.py
│
├── stream/                        # Streaming simulation
│   └── stream_generator.py
│
├── analytics/                     # Analytics engine
│   └── analytics.py
│
├── database/                      # Database operations
│   ├── load_data.py
│   └── query_examples.py
│
├── dashboard/                     # Streamlit dashboard
│   └── app.py
│
├── config/                        # Configuration
│   └── config.py
│
├── utils/                         # Utilities
│   └── logger.py
│
├── logs/                          # Application logs
│
├── notebooks/                     # Jupyter notebooks
│   ├── data_cleaning.ipynb
│   ├── eda.ipynb
│   └── feature_engineering.ipynb
│
├── requirements.txt
├── ridepulse.db                   # SQLite database
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/RidePulse.git
cd RidePulse
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the ETL pipeline:
```bash
python src/data_cleaning.py
python src/feature_engineering.py
```

4. Load data into database:
```bash
python database/load_data.py
```

5. Launch the dashboard:
```bash
streamlit run dashboard/app.py
```

The dashboard will be available at `http://localhost:8501`

## 📊 Key Insights

- **2.8M+ trips** analyzed from January 2025
- **$78.5M total revenue** generated
- **Peak hours**: 5-6 PM (200K+ trips)
- **Average fare**: $18.23
- **Average speed**: 11.65 mph
- **79% solo passengers**, highest revenue from multi-passenger trips

## 🛠️ Tech Stack

- **Languages**: Python
- **Data Processing**: Pandas, NumPy
- **Database**: SQLite
- **Visualization**: Streamlit, Plotly
- **Analysis**: Matplotlib, Seaborn
- **Logging**: Python logging module

## 📈 Database Schema

### fact_trips
Core trip records with all attributes (2.8M rows)

### kpi_hourly
Aggregated metrics by hour:
- total_revenue
- trip_count
- avg_fare
- avg_distance
- avg_speed

### kpi_passenger
Aggregated metrics by passenger count:
- trip_count
- total_revenue
- avg_fare

## 🎯 Future Enhancements

- [ ] Machine Learning models for fare and duration prediction
- [ ] Apache Kafka for real streaming
- [ ] Apache Spark for distributed processing
- [ ] PostgreSQL migration
- [ ] Docker containerization
- [ ] Apache Airflow for orchestration
- [ ] Real-time alerting system

## 📝 Resume Entry

**RidePulse: Real-Time Ride-Sharing Analytics Platform**

Developed a real-time analytics platform for ride-sharing events using NYC Taxi Trip data. Performed data cleaning, feature engineering, and streaming simulation to analyze trip patterns. Built an interactive Streamlit dashboard and integrated SQLite for persistent storage and SQL-based analytics. Generated insights on revenue trends, peak traffic hours, trip duration, and passenger distribution.

**Tech Stack**: Python, Pandas, SQLite, Streamlit, Matplotlib, Seaborn

## 👤 Author

Doredla Divya Sri - [GitHub](https://github.com/divyadoredla) | [LinkedIn](https://linkedin.com/in/divyadoredla24)

## 🙏 Acknowledgments

- NYC Taxi & Limousine Commission for the dataset
- Streamlit for the dashboard framework

Created with ❤️ by Doredla Divya Sri @2026


---

<div align="center">
  <p><strong>Created with ❤️ by Doredla Divya Sri @2026</strong></p>
  <p>RidePulse v1.0 | Data Engineering Portfolio Project</p>
</div>
