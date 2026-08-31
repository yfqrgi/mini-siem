# Mini SIEM & Log Analyzer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A lightweight modular Security Information and Event Management (SIEM) tool designed to parse Linux authentication logs, detect security anomalies (e.g., SSH Brute-Force attacks), store incident logs in a relational database, and visualize metrics via an interactive web dashboard

---

##  Features

- **Modular Architecture:** Clean separation of concerns with parsing, threat detection, persistent storage, and UI presentation layers
- **Log Parsing Engine:** Efficient extraction of authentication metrics from `sample_auth.log` files using Regular Expressions (Regex)
- **Rule-Based Threat Detection:** Automated identification of SSH brute-force patterns based on configurable thresholds
- **Persistent Storage:** Incident logging and audit trail using an SQLite relational database
- **Interactive Web Dashboard:** Real-time analytics, incident charts, search filters, and security KPIs powered by Streamlit

---

##  System Architecture

```text
+-------------------+      +-------------------+      +---------------------+
|  logs/auth.log    | ---> |   src/parser.py   | ---> |   src/detector.py   |
| (Raw System Log)  |      | (Regex Extraction)|      | (Threat Detection)  |
+-------------------+      +-------------------+      +---------------------+
                                                                 |
                                                                 v
+-------------------+      +-------------------+      +---------------------+
|   Streamlit UI    | <--- |  siem_events.db   | <--- |   src/database.py   |
| (app.py Dashboard)|      | (SQLite Storage)  |      |  (Data Insertion)   |
+-------------------+      +-------------------+      +---------------------+
```

## Repository Structure
```text
mini-siem/
├── logs/               # Sample log files for testing
│   └── sample_auth.log
├── src/                # Core application modules
│   ├── __init__.py
│   ├── database.py     # SQLite schema management and queries
│   ├── detector.py     # Threat detection logic engine
│   └── parser.py       # Regex log parser engine
├── .gitignore
├── app.py              # Interactive Streamlit web dashboard
├── main.py             # CLI entrypoint for analysis
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies
```

## Installation & Usage

1. Prerequisites
Ensure you have Python 3.10 or higher installed on your system

2. Clone the Repository

```bash
git clone [https://github.com/yfqrgi/mini-siem.git](https://github.com/yfqrgi/mini-siem.git)
cd mini-siem
```

3. Set Up Virtual Environment & Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. Run the Analyzer Engine (CLI)
Analyze system logs and update the database:

```bash
python3 main.py
```

5. Launch the Web Dashboard
Visualize metrics and historical security alerts:

```bash
streamlit run app.py
```

## Example CLI Output

```text
[*] Analyzing logs...

=== SAFETY WARNINGS ===
[ALERT] Brute-Force threat! IP: 192.168.1.100 -> 5 unsuccessful attempts

=== LATEST ALERTS ON DATABASE ===
ID: 2 | TIME: 2026-08-28 15:40:30 | IP: 192.168.1.100 | Attempts: 5 | Type: SSH Brute-Force
ID: 1 | TIME: 2026-08-27 16:22:42 | IP: 192.168.1.100 | Attempts: 5 | Type: SSH Brute-Force
```

## License
Distributed under the MIT License. See LICENSE for more information