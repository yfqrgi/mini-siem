from collections import Counter
from src.database import save_alert


def detect_brute_force(ip_count: Counter, threshold: int=3, save_to_db: bool = True):
    detected = False

    for ip, count in ip_count.items():
        if count >= threshold:
            print(f"[ALERT] Brute-Force threat! IP:{ip} {count} unsuccessfull attempts")
            if save_to_db:
                save_alert(ip, count, attack_type="SSH Brute-Force")
            detected = True

    if not detected:
        print("[INFO] No suspecious activitt was detected")