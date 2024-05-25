# PracticaSeguridadIA
Network Scanner
This Python script provides functionality for scanning devices on a network, detecting open ports, and determining the operating system of the devices. It utilizes the socket and scapy libraries for network operations.

# Requirements
Python 3.x
scapy library (pip install scapy)
# Usage
Clone the repository or download the script network_scanner.py.
Install the required dependencies using pip install -r requirements.txt.
Run the script using Python: python network_scanner.py.
Functionality
# 1. ARP Scan
The arp_scan function performs an ARP scan on the specified network interface and IP range. It discovers devices on the network along with their IP addresses, MAC addresses, and hostnames (if available).

# 2. Port Scan
The port_scan function scans for open ports on a specified target IP address. It supports scanning multiple ports simultaneously and identifies open ports using TCP SYN packets.

# 3. OS Detection
The detect_os function attempts to detect the operating system of a target device based on its open ports. Currently, it distinguishes between Linux/Unix and Windows systems based on common ports such as SSH, HTTP, and HTTPS.
