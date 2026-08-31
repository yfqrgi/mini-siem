# Mini SIEM & Log Analyzer

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A lightweight modular Security Information and Event Management (SIEM) CLI tool designed to parse Linux authentication logs, detect security anomalies (e.g., SSH Brute-Force attacks), and persist incident alerts in a relational database.

---

## Features

- **Modular Architecture:** Separate components for parsing, threat detection, and database storage.
- **Log Parsing:** Efficient extraction of metadata from Linux authentication logs (`auth.log`) using Regular Expressions (Regex).
- **Rule-Based Threat Detection:** Automated identification of SSH brute-force patterns based on configurable thresholds.
- **Persistent Storage:** Incident tracking using SQLite database with timestamped event logging.
- **Zero Heavy Dependencies:** Built using Python standard libraries (`re`, `sqlite3`, `collections`).

---

## System Architecture

```text
+-------------------+      +-------------------+      +---------------------+
|  logs/auth.log    | ---> |   src/parser.py   | ---> |   src/detector.py   |
| (Raw System Log)  |      |  (Regex Extraction)|      | (Threat Detection)  |
+-------------------+      +-------------------+      +---------------------+
                                                                 |
                                                                 v
+-------------------+                                 +---------------------+
|    Terminal /     | <------------------------------ |   src/database.py   |
|   CLI Output      |     (Query Saved Alerts)        |   (SQLite Storage)  |
+-------------------+                                 +---------------------+
```

## Repository Structure

```text
mini-siem/
├── logs/               # Sample log files for testing
│   └── sample_auth.log
├── src/                # Core application source code
│   ├── __init__.py
│   ├── database.py     # Database schema and SQLite queries
│   ├── detector.py     # Threat detection engine
│   └── parser.py       # Log parsing module using Regex
├── .gitignore
├── app.py
├── main.py             # CLI entrypoint
├── README.md           # Project documentation
└── requirements.txt
```

## Installation & Usage

1. Prerequisites
Ensure you have Python 3.10+ installed on your machine. No third-party packages required.

2. Clone the Repository
```bash
git clone [https://github.com/yfqrgi/mini-siem.git](https://github.com/yfqrgi/mini-siem.git)
cd mini-siem
```

3. Run the Analyzer
Execute the CLI application:
```bash
python3 main.py
```

### Example Output
```text
[*] Analyzing logs...

=== SAFETY WARNINGS ===
[ALERT] Brute-Force threat! IP:192.168.1.100 5 unsuccessfull attempts

=== LATEST ALERTS ON DATABASE ===
ID: 2 | TIME: 2026-08-28 15:40:30 | IP: 192.168.1.100 | Attempts: 5 | Type: SSH Brute-Force
ID: 1 | TIME: 2026-08-27 16:22:42 | IP: 192.168.1.100 | Attempts: 5 | Type: SSH Brute-Force