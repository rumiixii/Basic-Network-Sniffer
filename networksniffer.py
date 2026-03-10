#scapy is necessary for code simplification
from scapy.all import *
# function definition 
def process_packet(packet):
    #check if packet has IP layer 
    if packet.haslayer(IP):
   #extract the necessary information   
        source = packet[IP].src
        destination = packet[IP].dst
        protocol = packet[IP].proto

     #print source and destination ips
        if protocol == 6:
            protocol_name="TCP"
        elif protocol == 17: 
             protocol_name ="UDP"
        elif protocol == 1:
            protocol_name ="ICMP"
        else:
            protocol_name = "Other"


        print("Source Ip: "+ source)
        print("Destination Ip: " + destination)
        print("Protocol: " + protocol_name)
        print("=" * 40)

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("----------------------------------------")
            print("payload: " + str(payload))
        else:
            print("Payload: None")
    else:
        print("no source ip ")
    


#start sniffing
sniff(count=20, prn=process_packet)
