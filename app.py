import sqlite3
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Mini SIEM Dashboard", page_icon="#", layout="wide"
)

DB_PATH = "siem_events.db"


def load_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        query = "SELECT * FROM alerts ORDER BY timestamp DESC"
        df = pd.read_sql_query(query, conn)
        conn.close()

        if not df.empty:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except Exception as e:
        st.error(
            f"Error connecting to database: {e}. Make sure you run main.py first"
        )
        return pd.DataFrame()
