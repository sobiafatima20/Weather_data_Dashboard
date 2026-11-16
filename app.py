
import io
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# =========================================================
# 1. PAGE SETUP
# =========================================================
st.set_page_config(
    page_title="UK Weather Analytics",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# 2. PREMIUM LIGHT THEME CSS
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap');

:root {
    --bg: #F5F7FC;
    --white: #FFFFFF;
    --text: #25324B;
    --muted: #718096;
    --purple: #7356C8;
    --border: #E7EAF2;
}

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: var(--bg) !important;
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding: 2rem 3rem 3rem;
}

/* TEXT */
.stApp p,
.stApp label,
.stApp li,
.stMarkdown {
    color: var(--text);
}

h1, h2, h3, h4 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    color: #25324B !important;
    font-weight: 700 !important;
}

[data-testid="stCaptionContainer"] p {
    color: var(--muted) !important;
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid var(--border);
}

[data-testid="stSidebar"] > div {
    padding: 1.5rem 1rem;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #7356C8 !important;
}

[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: #34415C !important;
}

/* HERO */
.hero {
    background: linear-gradient(115deg, #7255C7, #557BC9, #409AA8);
    padding: 38px 40px;
    border-radius: 20px;
    margin-bottom: 28px;
    box-shadow: 0 10px 25px rgba(88, 93, 170, .13);
}

.hero h1 {
    color: white !important;
    font-size: 34px;
    margin: 0 0 10px;
}

.hero p {
    color: #F0F4FF !important;
    font-size: 15px;
    margin: 0;
}

/* SECTION TITLES */
.section-title {
    color: #34415C !important;
    font-size: 23px;
    font-weight: 800;
    font-family: 'Plus Jakarta Sans', sans-serif;
    margin-top: 35px;
    margin-bottom: 18px;
    padding-bottom: 12px;
    border-bottom: 1px solid #E1E5EF;
}

/* KPI CARDS */
[data-testid="stHorizontalBlock"] {
    gap: 18px;
}

.metric-card {
    background: #FFFFFF;
    padding: 24px 21px;
    border-radius: 16px;
    border: 1px solid #E8EAF2;
    min-height: 125px;
    box-shadow: 0 4px 15px rgba(35, 48, 85, .045);
    transition: all .25s ease;
}

.metric-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 9px 22px rgba(35, 48, 85, .09);
    border-color: #C9BDF0;
}

.metric-card .label {
    color: #718096 !important;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 14px;
}

.metric-card .value {
    color: #7356C8 !important;
    font-size: 28px;
    font-weight: 800;
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* QUESTION CARDS */
.question {
    background: #FFFFFF;
    padding: 21px 25px;
    border-radius: 14px;
    margin-top: 32px;
    margin-bottom: 18px;
    border: 1px solid #E8EAF2;
    border-left: 4px solid #8569D5;
    box-shadow: 0 3px 12px rgba(35, 48, 85, .035);
}

.question h3 {
    color: #34415C !important;
    font-size: 19px;
    margin: 0 0 9px;
}

.question p {
    color: #8569D5 !important;
    font-size: 12px;
    font-weight: 700;
    margin: 0;
}

/* CONCLUSION */
.conclusion {
    background: #F0EDFC;
    border-left: 4px solid #8569D5;
    padding: 17px 21px;
    border-radius: 10px;
    margin: 17px 0 28px;
    color: #34415C !important;
    font-size: 14px;
    line-height: 1.8;
}

.conclusion b {
    color: #7356C8 !important;
}

/* CHARTS */
[data-testid="stPlotlyChart"] {
    background: #FFFFFF;
    border: 1px solid #E8EAF2;
    border-radius: 16px;
    padding: 12px;
    margin: 12px 0 20px;
    box-shadow: 0 4px 15px rgba(35, 48, 85, .035);
}

/* INPUTS */
[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border-color: #DDE2ED !important;
    border-radius: 9px !important;
}

[data-baseweb="select"] span {
    color: #34415C !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"] {
    background: #FFFFFF !important;
}

[data-baseweb="menu"] li {
    color: #34415C !important;
}

[data-baseweb="input"] input,
[data-testid="stDateInput"] input {
    background: #FFFFFF !important;
    color: #34415C !important;
    border-color: #DDE2ED !important;
}

[data-testid="stCheckbox"] label p {
    color: #34415C !important;
}

/* DATAFRAME */
[data-testid="stDataFrame"] {
    border: 1px solid #E5E8F0;
    border-radius: 12px;
    overflow: hidden;
    background: #FFFFFF;
}

/* BUTTONS */
.stDownloadButton button {
    background: linear-gradient(110deg, #7356C8, #5285C8);
    color: white !important;
    border: none;
    border-radius: 10px;
    padding: 10px 22px;
    font-weight: 700;
}

.stDownloadButton button:hover {
    background: #6246B5;
    color: white !important;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: #FFFFFF;
    border: 1px dashed #B9B1D8;
    border-radius: 12px;
    padding: 12px;
}

[data-testid="stFileUploader"] p {
    color: #536078 !important;
}

/* ALERTS */
[data-testid="stAlert"] {
    border-radius: 12px;
}

/* DIVIDER */
hr {
    border-color: #E1E5EF !important;
}

/* RESPONSIVE */
@media(max-width: 900px) {
    .block-container {
        padding: 1rem 1.2rem 2rem;
    }

    .hero {
        padding: 25px 22px;
    }

    .hero h1 {
        font-size: 25px;
    }

    .metric-card {
        padding: 17px;
    }

    .metric-card .value {
        font-size: 22px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD CSV
# =========================================================
@st.cache_data
def load_data(file_bytes):
    df = pd.read_csv(io.BytesIO(file_bytes))
    df.columns = df.columns.str.strip()

    required = [
        "Formatted Date",
        "Temperature (C)",
        "Apparent Temperature (C)",
        "Wind Speed (km/h)",
        "Humidity",
        "Visibility (km)",
        "Pressure (millibars)"
    ]

    missing = [c for c in required if c not in df.columns]

    if missing:
        raise ValueError(
            "Missing columns: " + ", ".join(missing)
        )

    df["Formatted Date"] = pd.to_datetime(
        df["Formatted Date"],
        errors="coerce",
        utc=True
    )

    df = df.dropna(subset=["Formatted Date"]).copy()

    numeric_cols = [
        "Temperature (C)",
        "Apparent Temperature (C)",
        "Wind Speed (km/h)",
        "Humidity",
        "Visibility (km)",
        "Pressure (millibars)"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


# =========================================================
# 4. DATA SOURCE
# =========================================================
st.sidebar.title("🌦️ Weather Dashboard")
st.sidebar.caption("UK Historical Weather Analytics")

uploaded = st.sidebar.file_uploader(
    "Upload Weather CSV",
    type=["csv"]
)

try:
    if uploaded is not None:
        raw_original = load_data(uploaded.getvalue())
        source_name = uploaded.name

    else:
        with open("weather_data.csv", "rb") as f:
            raw_original = load_data(f.read())

        source_name = "weather_data.csv"

except FileNotFoundError:
    st.info(
        "Please upload weather_data.csv from the sidebar "
        "or place it in the same folder as app.py."
    )
    st.stop()

except Exception as e:
    st.error(f"CSV loading error: {e}")
    st.stop()

if raw_original.empty:
    st.error("The uploaded CSV contains no valid date records.")
    st.stop()


# =========================================================
# 5. DATA CLEANING
# =========================================================
before_cleaning = raw_original.drop_duplicates().copy()

cleaned = before_cleaning.copy()

# Replace zero pressure with missing values
cleaned["Pressure (millibars)"] = (
    cleaned["Pressure (millibars)"].replace(0, np.nan)
)

# Fill missing pressure with median
pressure_median = cleaned["Pressure (millibars)"].median()

if pd.notna(pressure_median):
    cleaned["Pressure (millibars)"] = (
        cleaned["Pressure (millibars)"].fillna(pressure_median)
    )


# =========================================================
# 6. SIDEBAR FILTERS
# =========================================================
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Dashboard Filters")

min_date = cleaned["Formatted Date"].min().date()
max_date = cleaned["Formatted Date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if isinstance(date_range, (tuple, list)):
    if len(date_range) == 2:
        start_date, end_date = date_range
    elif len(date_range) == 1:
        start_date = end_date = date_range[0]
    else:
        start_date, end_date = min_date, max_date
else:
    start_date = end_date = date_range

all_years = sorted(
    cleaned["Formatted Date"].dt.year.dropna().unique().tolist()
)

selected_years = st.sidebar.multiselect(
    "Select Year",
    all_years,
    default=all_years
)

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

selected_months = st.sidebar.multiselect(
    "Select Month",
    months,
    default=months
)


# =========================================================
# 7. FILTER FUNCTION
# =========================================================
def filter_weather(df):

    out = df.copy()

    out["_year_filter"] = out["Formatted Date"].dt.year
    out["_month_filter"] = out["Formatted Date"].dt.month_name()

    out = out[
        out["Formatted Date"].dt.date.between(
            start_date, end_date
        )
        & out["_year_filter"].isin(selected_years)
        & out["_month_filter"].isin(selected_months)
    ].copy()

    return out


filtered = filter_weather(cleaned)
raw_filtered = filter_weather(raw_original)

if filtered.empty:
    st.warning(
        "No data found for selected filters. "
        "Please change your date, year or month selection."
    )
    st.stop()


# =========================================================
# 8. HERO HEADER
# =========================================================
st.markdown("""
<div class="hero">
    <h1>🌦️ UK Weather Analytics Dashboard</h1>
           <p>A clear, interactive view of temperature, humidity, wind and changing weather patterns.
           Use the filters to explore the observations that matter to you.</p>
</div>
""", unsafe_allow_html=True)

st.caption(
    f"📁 Data Source: {source_name}   |   "
    f"📊 Filtered Observations: {len(filtered):,}"
)


# =========================================================
# 9. KPI CARDS
# =========================================================
st.markdown(
    '<div class="section-title">📌 Weather Overview</div>',
    unsafe_allow_html=True
)

avg_temp = filtered["Temperature (C)"].mean()
max_temp = filtered["Temperature (C)"].max()

avg_humidity_raw = filtered["Humidity"].mean()

avg_humidity_pct = (
    avg_humidity_raw * 100
    if pd.notna(avg_humidity_raw) and avg_humidity_raw <= 1
    else avg_humidity_raw
)

avg_wind = filtered["Wind Speed (km/h)"].mean()

kpis = [
    ("🌡️ Average Temperature",
     f"{avg_temp:.2f}°C" if pd.notna(avg_temp) else "N/A"),

    ("🔥 Highest Temperature",
     f"{max_temp:.2f}°C" if pd.notna(max_temp) else "N/A"),

    ("💧 Average Humidity",
     f"{avg_humidity_pct:.2f}%" if pd.notna(avg_humidity_pct) else "N/A"),

    ("🌬️ Average Wind Speed",
     f"{avg_wind:.2f} km/h" if pd.notna(avg_wind) else "N/A")
]

cols = st.columns(4)

for col, (label, value) in zip(cols, kpis):

    with col:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="label">{label}</div>
                <div class="value">{value}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# 10. CHART STYLE
# =========================================================
def show_chart(fig, height=410):

    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",

        font=dict(
            family="DM Sans",
            color="#34415C",
            size=12
        ),

        title=dict(
            x=0.5,
            font=dict(
                size=19,
                color="#263653"
            )
        ),

        height=height,

        margin=dict(
            l=35,
            r=30,
            t=65,
            b=40
        ),

        xaxis=dict(
            showgrid=True,
            gridcolor="#EDF0F6",
            zerolinecolor="#DDE3EE"
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#EDF0F6",
            zerolinecolor="#DDE3EE"
        ),

        hoverlabel=dict(
            bgcolor="#FFFFFF",
            font_color="#25324B"
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# 11. CONCLUSION HELPER
# =========================================================
def conclusion(message):

    st.markdown(
        f"""
        <div class="conclusion">
            <b>💡 Conclusion:</b> {message}
        </div>
        """,
        unsafe_allow_html=True
    )


def corr_strength(value):

    if pd.isna(value):
        return "could not be calculated"

    magnitude = abs(value)

    if magnitude < 0.20:
        strength = "very weak"
    elif magnitude < 0.40:
        strength = "weak"
    elif magnitude < 0.60:
        strength = "moderate"
    elif magnitude < 0.80:
        strength = "strong"
    else:
        strength = "very strong"

    direction = (
        "positive" if value > 0
        else "negative" if value < 0
        else "no"
    )

    return f"{strength} {direction}"


# =========================================================
# 12. QUESTION 1 - TEMPERATURE DISTRIBUTION
# =========================================================
st.markdown("""
<div class="question">
    <h3>Q1. What is the distribution of temperature in the UK weather dataset?</h3>
    <p>UNIVARIATE ANALYSIS</p>
</div>
""", unsafe_allow_html=True)

temp_values = filtered["Temperature (C)"].dropna()

fig = px.histogram(
    x=temp_values,
    nbins=30,
    title="Q1: Distribution of Temperature",
    labels={
        "x": "Temperature (°C)",
        "y": "Frequency"
    },
    color_discrete_sequence=["#9275DC"]
)

show_chart(fig)

temp_mean = temp_values.mean()
temp_median = temp_values.median()
temp_min = temp_values.min()
temp_max = temp_values.max()

if pd.notna(temp_mean):

    if temp_mean > temp_median:
        shape_note = "The distribution appears right-skewed."
    elif temp_mean < temp_median:
        shape_note = "The distribution appears left-skewed."
    else:
        shape_note = "The distribution appears fairly balanced."

    conclusion(
        f"Temperature ranges from {temp_min:.2f}°C to "
        f"{temp_max:.2f}°C. Mean temperature is "
        f"{temp_mean:.2f}°C and median is "
        f"{temp_median:.2f}°C. {shape_note}"
    )

else:
    conclusion("Temperature values are unavailable.")


# =========================================================
# 13. QUESTION 2 - HUMIDITY DISTRIBUTION
# =========================================================
st.markdown("""
<div class="question">
    <h3>Q2. What is the distribution of humidity in the dataset?</h3>
    <p>UNIVARIATE ANALYSIS</p>
</div>
""", unsafe_allow_html=True)

humidity_values = filtered["Humidity"].dropna()

humidity_plot = (
    humidity_values * 100
    if not humidity_values.empty and humidity_values.max() <= 1
    else humidity_values
)

fig = px.histogram(
    x=humidity_plot,
    nbins=30,
    title="Q2: Distribution of Humidity",
    labels={
        "x": "Humidity (%)",
        "y": "Frequency"
    },
    color_discrete_sequence=["#36B8AE"]
)

show_chart(fig)

humidity_mean = humidity_plot.mean()
humidity_median = humidity_plot.median()

if pd.notna(humidity_mean):

    conclusion(
        f"Average humidity is {humidity_mean:.2f}% "
        f"and median humidity is {humidity_median:.2f}%. "
        "The histogram displays the frequency of low, "
        "medium and high humidity observations."
    )

else:
    conclusion("Humidity values are unavailable.")


# =========================================================
# 14. QUESTION 3 - WIND SPEED DISTRIBUTION
# =========================================================
st.markdown("""
<div class="question">
    <h3>Q3. What is the distribution of wind speed in the dataset?</h3>
    <p>UNIVARIATE ANALYSIS</p>
</div>
""", unsafe_allow_html=True)

wind_values = filtered["Wind Speed (km/h)"].dropna()

fig = px.histogram(
    x=wind_values,
    nbins=30,
    title="Q3: Distribution of Wind Speed",
    labels={
        "x": "Wind Speed (km/h)",
        "y": "Frequency"
    },
    color_discrete_sequence=["#5599D5"]
)

show_chart(fig)

wind_mean = wind_values.mean()
wind_median = wind_values.median()

if pd.notna(wind_mean):

    conclusion(
        f"Average wind speed is {wind_mean:.2f} km/h "
        f"and median wind speed is {wind_median:.2f} km/h. "
        "The histogram displays the frequency of "
        "different wind-speed observations."
    )

else:
    conclusion("Wind speed values are unavailable.")


# =========================================================
# 15. QUESTION 4 - TEMPERATURE VS HUMIDITY
# =========================================================
st.markdown("""
<div class="question">
    <h3>Q4. Is there a relationship between temperature and humidity?</h3>
    <p>BIVARIATE ANALYSIS</p>
</div>
""", unsafe_allow_html=True)

q4_data = filtered[
    ["Temperature (C)", "Humidity"]
].dropna()

fig = px.scatter(
    q4_data,
    x="Temperature (C)",
    y="Humidity",
    color="Humidity",
    color_continuous_scale="Purples",
    opacity=0.55,
    title="Q4: Temperature vs Humidity",
    labels={
        "Temperature (C)": "Temperature (°C)",
        "Humidity": "Humidity"
    }
)

show_chart(fig)

corr_th = q4_data[
    "Temperature (C)"
].corr(q4_data["Humidity"])

if pd.notna(corr_th):

    relation = corr_strength(corr_th)

    if corr_th < -0.20:
        direction_text = (
            "As temperature increases, humidity tends to decrease."
        )
    elif corr_th > 0.20:
        direction_text = (
            "As temperature increases, humidity tends to increase."
        )
    else:
        direction_text = (
            "There is no clear linear pattern between temperature and humidity."
        )

    conclusion(
        f"Pearson correlation is {corr_th:.2f}, "
        f"indicating a {relation} relationship. "
        f"{direction_text} Correlation does not prove causation."
    )

else:
    conclusion("Temperature-humidity correlation could not be calculated.")


# =========================================================
# 16. QUESTION 5 - TEMPERATURE VS WIND SPEED
# =========================================================
st.markdown("""
<div class="question">
    <h3>Q5. Is there a relationship between temperature and wind speed?</h3>
    <p>BIVARIATE ANALYSIS</p>
</div>
""", unsafe_allow_html=True)

q5_data = filtered[
    ["Temperature (C)", "Wind Speed (km/h)"]
].dropna()

fig = px.scatter(
    q5_data,
    x="Temperature (C)",
    y="Wind Speed (km/h)",
    color="Wind Speed (km/h)",
    color_continuous_scale="Teal",
    opacity=0.55,
    title="Q5: Temperature vs Wind Speed",
    labels={
        "Temperature (C)": "Temperature (°C)",
        "Wind Speed (km/h)": "Wind Speed (km/h)"
    }
)

show_chart(fig)

corr_tw = q5_data[
    "Temperature (C)"
].corr(q5_data["Wind Speed (km/h)"])

if pd.notna(corr_tw):

    relation = corr_strength(corr_tw)

    if abs(corr_tw) < 0.20:
        explanation = (
            "The points show little linear association between the variables."
        )
    elif corr_tw > 0:
        explanation = (
            "Higher temperatures tend to be associated with higher wind speeds."
        )
    else:
        explanation = (
            "Higher temperatures tend to be associated with lower wind speeds."
        )

    conclusion(
        f"Pearson correlation is {corr_tw:.2f}, "
        f"indicating a {relation} relationship. "
        f"{explanation} This does not establish causation."
    )

else:
    conclusion("Temperature-wind-speed correlation could not be calculated.")


# =========================================================
# 17. CORRELATION HEATMAP
# =========================================================
st.markdown(
    '<div class="section-title">🔗 Correlation Heatmap</div>',
    unsafe_allow_html=True
)

weather_columns = [
    "Temperature (C)",
    "Apparent Temperature (C)",
    "Wind Speed (km/h)",
    "Humidity",
    "Visibility (km)",
    "Pressure (millibars)"
]

corr = filtered[weather_columns].corr(numeric_only=True)

fig = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    title="Correlation Between Weather Variables"
)

show_chart(fig, 480)

if len(weather_columns) >= 2:

    corr_abs = corr.abs().copy()

    corr_values = corr_abs.to_numpy(copy=True)

    np.fill_diagonal(corr_values, np.nan)

    corr_abs = pd.DataFrame(
        corr_values,
        index=corr.index,
        columns=corr.columns
    )

    if corr_abs.notna().any().any():

        strongest_pair = corr_abs.stack().idxmax()

        strongest_value = corr.loc[
            strongest_pair[0],
            strongest_pair[1]
        ]

        conclusion(
            f"The strongest correlation is between "
            f"{strongest_pair[0]} and {strongest_pair[1]} "
            f"(r = {strongest_value:.2f}). "
            "Values near +1 indicate positive association, "
            "values near -1 indicate negative association, "
            "and values near 0 indicate weak linear association."
        )

    else:
        conclusion(
            "There are not enough valid numeric pairs "
            "to identify the strongest correlation."
        )


# =========================================================
# 18. TEMPERATURE OVER TIME
# =========================================================
st.markdown(
    '<div class="section-title">📈 Temperature Over Time</div>',
    unsafe_allow_html=True
)

daily_temperature = (
    filtered.set_index("Formatted Date")["Temperature (C)"]
    .resample("D")
    .mean()
    .dropna()
    .reset_index()
)

fig = px.line(
    daily_temperature,
    x="Formatted Date",
    y="Temperature (C)",
    title="Daily Average Temperature Over Time",
    color_discrete_sequence=["#8062D6"],
    labels={
        "Formatted Date": "Date",
        "Temperature (C)": "Temperature (°C)"
    }
)

fig.update_traces(
    line=dict(width=2.5),
    mode="lines"
)

show_chart(fig)

if not daily_temperature.empty:

    highest_day = daily_temperature.loc[
        daily_temperature["Temperature (C)"].idxmax()
    ]

    lowest_day = daily_temperature.loc[
        daily_temperature["Temperature (C)"].idxmin()
    ]

    conclusion(
        f"Highest daily average temperature was "
        f"{highest_day['Temperature (C)']:.2f}°C on "
        f"{highest_day['Formatted Date'].date()}, "
        f"while the lowest was "
        f"{lowest_day['Temperature (C)']:.2f}°C on "
        f"{lowest_day['Formatted Date'].date()}."
    )

else:
    conclusion("Daily temperature values are unavailable.")


# =========================================================
# 19. MONTHLY AVERAGE TEMPERATURE
# =========================================================
st.markdown(
    '<div class="section-title">📅 Monthly Average Temperature</div>',
    unsafe_allow_html=True
)

monthly = filtered.copy()

monthly["Month Number"] = (
    monthly["Formatted Date"].dt.month
)

monthly["Month Name"] = (
    monthly["Formatted Date"].dt.month_name()
)

monthly_temperature = (
    monthly.groupby(
        ["Month Number", "Month Name"],
        as_index=False
    )["Temperature (C)"]
    .mean()
    .sort_values("Month Number")
)

fig = px.bar(
    monthly_temperature,
    x="Month Name",
    y="Temperature (C)",
    title="Average Temperature by Month",
    color="Temperature (C)",
    color_continuous_scale="Purples",
    labels={
        "Month Name": "Month",
        "Temperature (C)": "Average Temperature (°C)"
    }
)

fig.update_layout(
    coloraxis_showscale=False
)

fig.update_traces(
    marker_line_width=0,
    opacity=0.9
)

show_chart(fig)

if not monthly_temperature.empty:

    warmest = monthly_temperature.loc[
        monthly_temperature["Temperature (C)"].idxmax()
    ]

    coldest = monthly_temperature.loc[
        monthly_temperature["Temperature (C)"].idxmin()
    ]

    conclusion(
        f"{warmest['Month Name']} has the highest monthly "
        f"average temperature ({warmest['Temperature (C)']:.2f}°C), "
        f"while {coldest['Month Name']} has the lowest "
        f"({coldest['Temperature (C)']:.2f}°C) "
        "in the selected data."
    )

else:
    conclusion("Monthly temperature averages are unavailable.")


# =========================================================
# 20. RAW DATA
# =========================================================
st.markdown(
    '<div class="section-title">🗂️ Raw Data Explorer</div>',
    unsafe_allow_html=True
)

if st.checkbox("Show Raw Data"):

    preferred_columns = [
        "Formatted Date",
        "Time",
        "Temperature (C)",
        "Apparent Temperature (C)",
        "Wind Speed (km/h)",
        "Humidity",
        "Visibility (km)",
        "Pressure (millibars)",
        "Month"
    ]

    # Display only columns actually available in the CSV
    raw_columns = [
        c for c in preferred_columns
        if c in raw_filtered.columns
    ]

    raw_display = raw_filtered[raw_columns].copy()

    st.dataframe(
        raw_display,
        use_container_width=True,
        height=380
    )

    csv_data = raw_display.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Raw Filtered Data",
        data=csv_data,
        file_name="weather_data_filtered.csv",
        mime="text/csv"
    )


# =========================================================
# 21. FOOTER
# =========================================================
st.markdown("---")

st.markdown(
    """
    <div style="
        text-align:center;
        padding:15px;
        color:#8792A7;
        font-size:12px;
        font-family:'DM Sans',sans-serif;
    ">
        <b style="color:#7356C8;">
            🌦️ UK WEATHER ANALYTICS
        </b>
        <br><br>
        Built with Streamlit, Pandas, NumPy and Plotly
        <br>
        Interactive Historical Weather Data Analysis
    </div>
    """,
    unsafe_allow_html=True
)
