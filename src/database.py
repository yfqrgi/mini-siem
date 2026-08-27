import sqlite3
from datetime import datetime

DB_NAME = "siem_events.db"


def init_db():
    """Baza va jadvalni yaratadi."""
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