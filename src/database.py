import sqlite3
from datetime import datetime

DB_NAME = "siem_events.db"


def init_db():
    """"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            attempts INTEGER NOT NULL,
            attack_type TEXT NOT NULL
        )
    """
    )

    conn.commit()
    conn.close()


def save_alert(ip_address: str, attempts: int, attack_type: str = "SSH Brute-Force"):
    """"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO alerts (timestamp, ip_address, attempts, attack_type)
        VALUES (?, ?, ?, ?)
    """,
        (now, ip_address, attempts, attack_type),
    )

    conn.commit()
    conn.close()


def get_all_alerts():
    """"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts ORDER BY timestamp DESC")
    rows = cursor.fetchall()

    conn.close()
    return rows