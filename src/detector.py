from collections import Counter
from src.database import save_alert


def detect_brute_force(ip_count: Counter, threshold: int=3, save_to_db: bool = True):
    detect = False

    for ip, count in ip_count.items():
        if count >= threshold:
            print(f"[ALERT] Brute-Force threat! IP:{ip} {count} unsuccessfull attempts")
            if save_to_db:
                save_alert(ip, count, attack_type="SSH Brute-Force")
            detect = True

    if not detect:
        print("[INFO] No suspecious activitt was detected")