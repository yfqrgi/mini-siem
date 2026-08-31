from src.database import get_all_alerts, init_db
from src.detector import detect_brute_force
from src.parser import parse_ssh_logs

LOG_FILE = "logs/sample_auth.log"


def main():
    print("==================================================")
    print("         MINI SIEM & LOG ANALYZER ENGINE          ")
    print("==================================================\n")

    init_db()

    print(f"[*] '{LOG_FILE}' Analyzing logs...")
    ip_counts = parse_ssh_logs(LOG_FILE)

    print("\n=== SAFETY WARNINGS ===")
    detect_brute_force(ip_counts, threshold=3, save_to_db=True)

    print("\n=== LATEST ALERTS ON DATABASE ===")
    alerts = get_all_alerts()

    if alerts:
        for alert in alerts[:5]:
            print(
                f"ID: {alert[0]} | TIME: {alert[1]} | IP: {alert[2]} | Attempts: {alert[3]} | Type: {alert[4]}"
            )
    else:
        print("[INFO] There are no alerts in the database yet.")

    print("\n==================================================")
    print("   IN TUPERMINAL TO VIEW THE WEB DASHBOARD:")
    print("   streamlit run app.py")
    print("==================================================\n")


if __name__ == "__main__":
    main()