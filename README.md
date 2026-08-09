# Basic Network Sniffer

 Project Overview

This project is a Python-based Basic Network Sniffer developed as part of the CodeAlpha Cyber Security Internship.

The program captures network packets and analyzes important information such as source IP address, destination IP address, network protocol, packet size, and payload information.

 Objectives

- Capture network traffic packets using Python.
- Analyze the structure of captured packets.
- Identify common network protocols.
- Display source and destination IP addresses.
- Display packet size and payload information.
- Summarize captured traffic based on protocols.

 Technologies Used

- Python 3
- Scapy
- Command Prompt
- Windows

 Features

- Real-time packet capture
- Source IP detection
- Destination IP detection
- TCP, UDP and ICMP protocol identification
- Packet size analysis
- Payload detection and hexadecimal preview
- Protocol statistics
- Timestamp for captured packets

 How It Works

The program uses the Scapy library to capture network packets.

For each IP packet, the program extracts:

1. Timestamp
2. Source IP address
3. Destination IP address
4. Protocol
5. Packet size
6. Payload size
7. Payload preview

After capturing the configured number of packets, the program displays a protocol summary.

How to Run

Install Scapy:

```bash
pip install scapy
