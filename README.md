# Basic-Network-Sniffer
# Requirements 
 - Python 3.12
 - Scapy
 - Npcap(Windows Only)
## What is a Network Sniffer and Why is it useful? 
A network sniffer allows one to assess the packets being sent across networks. The information needed are; the source IP address, Destination IP address, the protocol used and the payload, all of which are important in helping to secure a network. 
## How it works
In order to design one that could output those information, I used Scapy, a Python library used for network packet manipulation. Npcap is also required on Windows as it acts as a bridge between Scapy and the network card, allowing Python to access raw network packets. 
The logic behind my code: 
- Import Scapy to support the networking aspect of the project.
- Create a function that would process the packet. Within this function
   - Begin by checking whether the packet has an IP layer, since not all packets contain IP addresses
   - If it does, extract the source IP,destination IP and protocol number and convert the protocol number into a readable name (TCP,UDP,ICMP or OTHER)
   - Check if the packet contains a payload and dislay it, otherwise display none
 - Call Scapy's sniff() function, specifying how many packets to capture and which function to run for each packet
## How to run 
 1. Install dependencies: pip install scapy
 2. Install Npcap from https://npcap.com
 3. Run Vs code or your chosen IDE as Admininstrator
 4. Run the script: python networksniffer.py
