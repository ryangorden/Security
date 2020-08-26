"""These script was to create to test against my CCNP Security lab.
   They are not intended for malicious use. If used to attack any system
   without authorization from that company/user means you are performing 
   an illegal act. Please act responsibly.""" 

import subprocess
import sys

interface= sys.argv[1]
mac_address= sys.argv[2]

def change_mac(interface, mac_address):
    print('Changing the MAC Address for', interface, 'to', mac_address)
    subprocess.call(['ip', 'link', 'set', interface,'down']) #ifcong eth0 down can be used as well
    subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
    subprocess.call(['ip', 'link', 'set', interface,'up'])
    return 'Mac Address has been changed to ' + mac_address

if __name__ == '__main__':
    notification= change_mac(interface, mac_address)
    print(notification)
