import subprocess
#run system commands via script
import optparse
#used to add input args on single line
import re 
#used to detect reg exp

def change_mac(interface,new_mac):
    #subprocess.call("COMMAND",shell=True)
    print("[+] Change MAC Address of "+ interface+ " to "+new_mac)
    #change MAC Address
    subprocess.run(["ifconfig",interface,"down"],shell=True) 
    subprocess.run(["ifconfig",interface,"hw","ether", new_mac],shell=True) 
    subprocess.run(["ifconfig",interface,"up"],shell=True) 
    subprocess.run(["ifconfig",interface],shell=True) 

#set interface and mac variables
#parse variables on single line
def get_args():
    parser=optparse.OptionParser()
    #create options
    parser.add_option("-i","--interface",dest="interface",help="Choose interface (ex.wlan0)")
    parser.add_option("-m","--mac",dest="new_mac",help = "Choose new MAC (ex. 00:11:22:33:44:55)")
    (options,arguments)= parser.parse_args()
    if not options.interface:
        parser.error("[ERROR] no interface value found")
    elif not options.new_mac:
        parser.error("[ERROR] no new mac value found")
    return options

def get_current_mac(interface):
    #check output of command 
    output=subprocess.check_output(["ifconfig",interface])
    mac_res=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
    if(mac_res):
        print(mac_res)
    else:
        print("[+] UNREADABLE MAC ADDRESS   ")
        
        
#main code
options= get_args()
change_mac(options.interface,options.new_mac)
curr_mac=get_current_mac(options.interface)
if curr_mac==options.new_mac:
    print("[+] MAC Change Complete")
else:
    print("[ERROR] MAC did not change")
