# Basic-Network-Sniffer
# Requirements 
 - Python 3.12
 - Scapy
 - Npcap(Windows Only)
## What is a Network Sniffer and Why is it useful? 
A network sniffer allows one to assess the packets being sent across networks. The information needed are; the source IP address, Destination IP address, the protocol used and the payload, all of which are important in helping to secure a network. 
## How it works
In order to design one that could output those information, I used Scapy, a Python library used for network packet manipulation. Npcap is also required on Windows as it acts as a bridge between Scapy and the network card, allowing Python to access raw network packets. 
The logic behind my code is 
  A) Import Scapy to support the networking aspect of the project. 
  B) Create a function that would process the packet; 
      Within this function, Create nested conditions to capture the source and destination IP addresses, the protocol used ( whether it is TCP, UDP,ICMP or "Other" ) and the payload. The payload is important because it helps us in analyzing the packet and determining whether it is malicious or not 

## How to run 
 1. Install dependencies: pip install scapy
 2. Install Npcap from https://npcap.com
 3. Run Vs code or your chosen IDE as Admininstrator
 4. Run the script: python networksniffer.py
