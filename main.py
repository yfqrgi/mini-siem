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

    