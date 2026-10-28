from pathlib import Path

log_file = Path(__file__).parent / "logs" / "sample_auth.log"

failed_attempts = 0

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        if "Failed password" in line:
            failed_attempts = failed_attempts + 1
            print(line.strip())

print("Total failed login attempts:", failed_attempts)

print("\n=== IP ADDRESS ANALYSIS ===")

ip_counts = {}

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip_address = parts[parts.index("from") + 1]

            if ip_address in ip_counts:
                ip_counts[ip_address] += 1
            else:
                ip_counts[ip_address] = 1

for ip, count in ip_counts.items():
    print("IP Address:", ip)
    print("Failed Attempts:", count)

    if count >= 3:
        print("SECURITY ALERT: Repeated failed logins detected!")