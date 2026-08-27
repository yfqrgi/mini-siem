from collections import Counter
import re


def parser_ssh_logs(log_path: str) -> Counter:
    pattern = r"Failed password for .* from (?P<ip>\d+\.\d+\.\d+\.\d+)"
    failed_attempts = []

    try:
        with open(log_path, "r") as file:
            for line in file:
                math = re.search(pattern, line)
                if math:
                    failed_attempts.append(math.group("ip"))

    except FileNotFoundError:
        print(f"[Error] Log file not found: {log_path}")

    return Counter(failed_attempts)