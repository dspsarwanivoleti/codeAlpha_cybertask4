# codeAlpha_cybertask4
task 4: intrusion
# NetGuard IDS - Network Intrusion Detection System

## Overview

NetGuard IDS is a Python-based Network Intrusion Detection System (IDS) designed to monitor network traffic and detect suspicious activities in real time. The system analyzes packets, identifies potential attacks, generates alerts, logs incidents, and provides visualization of detected threats.

This project demonstrates practical cybersecurity concepts including packet analysis, intrusion detection, attack logging, and alert generation.

---

## Features

* Real-time network traffic monitoring
* Ping Flood Detection
* SYN Flood Detection
* Port Scan Detection
* Attack Logging to CSV
* Email Alert Notifications
* Attack Visualization Dashboard
* Security Event Tracking

---

## Technologies Used

* Python
* Scapy
* Pandas
* Matplotlib
* CSV Logging
* SMTP Email Alerts
* Npcap (Windows)

---

## Project Structure

NetGuard_IDS/

├── ids.py

├── dashboard.py

├── attack_log.csv

├── screenshots/

├── README.md



---

## Installation

### Clone Repository

git clone <repository_url>

cd NetGuard_IDS

### Install Dependencies

pip install scapy pandas matplotlib

### Windows Users

Install Npcap:

https://npcap.com/

During installation, enable:

* Install Npcap in WinPcap API-Compatible Mode

Restart the system after installation.

---

## Running the IDS

Run the intrusion detection system:

python ids.py

The IDS will begin monitoring network traffic and detecting suspicious activity.

---

## Running the Dashboard

python dashboard.py

The dashboard displays a graphical representation of detected attacks.

---

## Detection Rules

### Ping Flood Detection

Detects excessive ICMP packets from a single source.

### SYN Flood Detection

Detects abnormal numbers of TCP SYN requests.

### Port Scan Detection

Detects attempts to scan multiple destination ports from the same source IP.

---

## Email Alert System

When an attack is detected, the IDS sends an email notification containing:

* Attack Type
* Source IP Address
* Timestamp

Example:

Subject: IDS Alert - Port Scan Detected

Attack Type: Port Scan

Source IP: 192.168.1.5

Immediate investigation recommended.

---

## Attack Log Format

The IDS stores events in attack_log.csv.

Example:

Timestamp,IP,Attack

2026-06-08 10:25:11,192.168.1.5,Port Scan

2026-06-08 10:30:42,192.168.1.5,SYN Flood

---

## Sample Output

[ALERT] Port Scan Detected from 192.168.1.5

[EMAIL ALERT SENT]

[ALERT] SYN Flood Detected from 192.168.1.5

---

## Future Enhancements

* Web-based Dashboard
* Machine Learning Attack Detection
* GeoIP Tracking
* Severity-Based Alerts
* Telegram Notifications
* Real-Time Threat Intelligence Integration

---

## Learning Outcomes

Through this project, users gain knowledge of:

* Network Security
* Packet Analysis
* Intrusion Detection Systems
* Cyber Threat Monitoring
* Security Event Logging
* Security Alerting Mechanisms

---

## Author

D S P SARWANI VOLETI

Cybersecurity Project – Network Intrusion Detection System (NIDS)

Academic/Portfolio Project

