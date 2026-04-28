import pandas as pd
import glob
import os
import streamlit as st

@st.cache_data
def load_and_merge_data(data_path='data/*_clean.csv'):
    """Finds all cleaned CSVs and merges them into a single Tidy DataFrame."""
    files = glob.glob(data_path)
    all_data = []
    
    for file in files:
        df = pd.read_csv(file)
        # Extract country name from filename
        country = os.path.basename(file).split('_')[0].capitalize()
        df['Country'] = country
        
        # Standardize Date column
        date_col = 'Date' if 'Date' in df.columns else 'DATE'
        if date_col in df.columns:
            df['Date'] = pd.to_datetime(df[date_col])
        
        all_data.append(df)
    
    if not all_data:
        return pd.DataFrame() # Return empty if no files found
        
    return pd.concat(all_data)

def get_monthly_averages(df, country_list, variable, year_range):
    """Filters data and resamples to monthly averages."""
    # Filter by country and year
    filtered = df[
        (df['Country'].isin(country_list)) & 
        (df['Date'].dt.year >= year_range[0]) & 
        (df['Date'].dt.year <= year_range[1])
    ]
    
    # Resample
    monthly = filtered.groupby(['Country', pd.Grouper(key='Date', freq='ME')])[variable].mean().reset_index()
    return monthly