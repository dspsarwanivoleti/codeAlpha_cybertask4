from scapy.all import *
from collections import defaultdict
import csv
import time

icmp_counter = defaultdict(int)
syn_counter = defaultdict(int)
port_scan = defaultdict(set)

THRESHOLD = 20

def log_attack(ip, attack):

    with open("attack_log.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            time.strftime("%Y-%m-%d %H:%M:%S"),
            ip,
            attack
        ])

def detect(packet):

    if packet.haslayer(IP):

        src = packet[IP].src

        # ICMP Detection
        if packet.haslayer(ICMP):

            icmp_counter[src] += 1

            if icmp_counter[src] > THRESHOLD:

                print(
                    f"[ALERT] Possible Ping Flood from {src}"
                )

                log_attack(
                    src,
                    "Ping Flood"
                )

        # SYN Flood Detection
        if packet.haslayer(TCP):

            if packet[TCP].flags == "S":

                syn_counter[src] += 1

                if syn_counter[src] > THRESHOLD:

                    print(
                        f"[ALERT] Possible SYN Flood from {src}"
                    )

                    log_attack(
                        src,
                        "SYN Flood"
                    )

        # Port Scan Detection
        if packet.haslayer(TCP):

            port_scan[src].add(
                packet[TCP].dport
            )

            if len(port_scan[src]) > 10:

                print(
                    f"[ALERT] Port Scan Detected from {src}"
                )

                log_attack(
                    src,
                    "Port Scan"
                )

print("="*50)
print("NetGuard IDS Started")
print("="*50)

sniff(
    prn=detect,
    store=False
)