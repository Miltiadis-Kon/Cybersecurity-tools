# Cybersecurity-tools
A plethora of algorithms to automate basic cybersecurity tasks


## ARP SPOOFING.

1) Pretend to be the router.
    A) arp-a --> see your interface and router IP.
    A) arpspoof -i eth0 -t (router ip ) (target ip) --> Update arp table to tell router that I am target

2) Pretend to be the target.
    arpspoof -i eth0 -t (target ip ) (router ip) --> Update arp table to tell target that I am router

3) Port Forwarding 
    A) echo 1 > /proc/sys/net/ipv4/ip_forward 
    
    ## DNS Spoofing
    
    ### Explanation
    A method to sniff packets and forward user to a custom server when a specific DNS request is send.
    DNS spoof works ONLY if you are the man in the middle..
    (ex. If users browses www.facebook.com, then redirect him to your apache server.) 
    
    ### Complete use case
    1) Stalk user's behviour (find his/her favourite websites).
    2) Create a clone of the website and run server.
    3) Run arp-spoof.py to be the man in the middle
    4) Run dns-spoof.py to her favourite website
    5) Wait for her to connect and she will be redirected to your website.
    6) Steal her data.
    
