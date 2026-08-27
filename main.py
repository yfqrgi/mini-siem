from src.database import get_all_alerts, init_db
from src.detector import detect_brute_force
from src.parser import parser_ssh_logs

LOG_FILE = "logs/sample_auth.log"


def main():

    init_db()

    print("[*] Analyzing logs...")
    ip_counts = parser_ssh_logs(LOG_FILE)

    print("\n=== SAFETY WARNINGS ===")
    detect_brute_force(ip_counts, threshold=3)

    print("\n=== LATEST ALERTS ON DATABASE ===")
    alerts = get_all_alerts()
    for alert in alerts:
        print(f"ID: {alert[0]} | TIME: {alert[1]} | IP: {alert[2]} | Attempts: {alert[3]} | Type: {alert[4]}")


if __name__ == "__main__":
    main()