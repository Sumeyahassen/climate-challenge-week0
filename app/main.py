import streamlit as st
import plotly.express as px # type: ignore
from utils import load_and_merge_data, get_monthly_averages

# Page setup
st.set_page_config(page_title="African Climate Dashboard", layout="wide")

st.title("🌍 Climate Trend Dashboard")

# 1. Load Data
df = load_and_merge_data(data_path='data/*_clean.csv')

if df.empty:
    st.warning("No data found in ../data/ folder. Please check file paths.")
else:
    # 2. Sidebar Controls
    st.sidebar.header("Dashboard Settings")
    
    countries = st.sidebar.multiselect("Select Countries", options=df['Country'].unique(), default=df['Country'].unique())
    
    var_options = {"T2M": "Temp", "PRECTOTCORR": "Rainfall", "RH2M": "Humidity"}
    selected_var = st.sidebar.selectbox("Variable", options=list(var_options.keys()), format_func=lambda x: var_options[x])
    
    years = st.sidebar.slider("Years", int(df['Date'].dt.year.min()), int(df['Date'].dt.year.max()), (2015, 2026))

    # 3. Process & Plot
    plot_df = get_monthly_averages(df, countries, selected_var, years)
    
    if not plot_df.empty:
        fig = px.line(plot_df, x='Date', y=selected_var, color='Country', 
                      title=f"Monthly {var_options[selected_var]} Trends",
                      template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Select a country to view trends.")