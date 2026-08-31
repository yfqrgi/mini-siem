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


col_title, col_refresh = st.columns([4, 1])
with col_title:
    st.title("Mini SIEM & Threat Detection Dashboard")
    st.caption(
        "Real-time log analysis and anomaly monitoring dashboard"
    )

with col_refresh:
    st.write("")
    if st.button("Update data", use_container_width=True):
        st.rerun()

df = load_data()

if df.empty:
    st.warning("There are no warnings in the database yet")
else:
    st.divider()

    total_alerts = len(df)
    unique_ips = df["ip_address"].nunique()
    total_attempts = df["attempts"].sum()
    top_attacker = df["ip_address"].mode()[0] if not df.empty else "N/A"

    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="Total Warnings (Alerts)", value=total_alerts)
    m2.metric(label="Number of suspicious IPs", value=unique_ips)
    m3.metric(label="Common Unsuccessful Attempts", value=total_attempts)
    m4.metric(label="Most active attacker IP", value=top_attacker)

    st.divider()

    g1, g2 = st.columns(2)

    with g1:
        st.subheader("Top Attacker IP Addresses")
        ip_counts = (
            df.groupby("ip_address")["attempts"]
            .sum()
            .reset_index()
            .sort_values(by="attempts", ascending=False)
        )

    with g1:
        st.subheader("Distribution by attack type")
        attack_type_counts = df["attack_type"].value_counts()
        st.bar_chart(data=attack_type_counts, color="#FFA500")

    st.divider()

    st.subheader("All Alert History")

    search_ip = st.text_input("Search by IP address:", "")

    filtered_df = df.copy()
    if search_ip:
        filtered_df = filtered_df[
            filtered_df["ip_address"].str.contains(search_ip, case=False)
        ]

    st.dataframe(
        filtered_df,
        column_config={
            "id": "ID",
            "timestamp": st.column_config.DatetimeColumn(
                "Time", format="YYYY-MM-DD HH-mm:ss"
            ),
            "ip_address": "IP Address",
            "attempts": "Number of Attempts",
            "attack_type": "Attack Type"
        },
        use_container_width=True,
        hide_index=True,
    )