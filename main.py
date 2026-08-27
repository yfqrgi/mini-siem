from collections import Counter
import re

LOG_FILE_PATH = "logs/sample_auth.log"
BRUTE_FORCE_THRESHOLD = 3

def parse_and_detect(log_path):
    pattern = r"Failed password for .* from (?P<ip>\d+\.\d+\.\d+\.\d+)"

    failed_attempts = []

    print("[*] Analyzing log file...\n")

    with open(log_path, "r") as file:
        for line in file:
            math = re.search(pattern, line)
            if math:
                ip = math.group("ip")
                failed_attempts.append(ip)

    ip_count = Counter(failed_attempts)

    print("=== SAFETY WARNINGS (ALERTS) ===")
    detect = False
    for ip, count in ip_count.items():
        if count >= BRUTE_FORCE_THRESHOLD:
            print(
                f"[ALERT] SSH Brute-Force vulnerability detected! IP: {ip} -> {count} unsuccessful attempts"
            )
            detect = True

    if not detect:
        print("[INFO] No suspicious activity detected")


if __name__ == "__main__":
    parse_and_detect(LOG_FILE_PATH)