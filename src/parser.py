import re
from datetime import datetime

def parser_log_line(line: str):

    pattern = r"^(\w{3} \d+ \d+:\d+:\d+) .*sshd.* (Failed|Accepted) password for (?:invalid user )?(\w+) from ([\d\.]+)"

    match = re.search(pattern, line)
    if not match:
        return None

    timestamp_str, status_raw, username, ip = match.groups()

    try:
        timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")
        timestamp = timestamp.replace(year=datetime.now().year())
    except ValueError:
        return None

    return {
        "source_ip": ip,
        "username": username,
        "action": "login_attemps",
        "status": status_raw.lower(),
        "timestamp": timestamp
    }