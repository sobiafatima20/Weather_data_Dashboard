# UK Weather Analytics Dashboard

A Streamlit-based data analytics project for exploring historical UK weather data. This app helps users analyze patterns in temperature, humidity, wind speed, visibility, and pressure using interactive charts, summary metrics, and filtering tools.

## Overview

The dashboard loads weather records from a CSV file (or the bundled dataset) and presents:

- KPI summary cards for average temperature, maximum temperature, humidity, and wind speed
- Histograms for univariate analysis of weather variables
- Scatter plots to study relationships between temperature and other metrics
- Correlation heatmap for major weather features
- Time-series view of temperature trends over time
- Monthly average temperature analysis
- Raw data explorer with CSV download option

## Project Structure

- `app.py` — Streamlit dashboard application
- `weather_data.csv` — sample UK weather dataset used by default
- `Analyze_and_visualize_historical_weather_data.ipynb` — exploratory notebook for analysis work
- `requirements.txt` — Python dependency list

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Jupyter Notebook

## Features

- Flexible date, year, and month filtering from the sidebar
- CSV upload support for custom weather datasets
- Cleaned and validated numeric columns
- Insight-driven conclusions generated alongside charts
- Download filtered dataset as CSV

## Setup Instructions

1. Clone or download this project.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the dashboard:

   ```bash
   streamlit run app.py
   ```

6. Open the local URL shown in the terminal, usually:

   ```text
   http://localhost:8501
   ```

## Data

The dashboard expects a CSV file containing weather-related columns such as:

- `Formatted Date`
- `Time`
- `Temperature (C)`
- `Apparent Temperature (C)`
- `Wind Speed (km/h)`
- `Humidity`
- `Visibility (km)`
- `Pressure (millibars)`
- `Month`

If `weather_data.csv` is present in the project folder, it will be used automatically. You can also upload your own CSV from the sidebar.

## Usage

- Select date range, year, and month filters from the left sidebar.
- Explore summary metrics and chart-based insights in the main dashboard.
- Toggle the raw data view to inspect records and download the filtered dataset.

## License

This project is intended for educational and analytical use.
