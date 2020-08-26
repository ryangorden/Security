"""These script was to create to test against my CCNP Security lab.
   They are not intended for malicious use. If used to attack any system
   without authorization from that company/user means you are performing 
   an illegal act. Please act responsibly.""" 

import subprocess
import sys

def get_arguments():
    arguments= {
                'interface': sys.argv[1],
                'mac_address': sys.argv[2]
               }
    return arguments

def change_mac(arguments):
    print('Changing the MAC Address for', arguments['interface'], 'to', arguments['mac_address'])
    subprocess.call(['ip', 'link', 'set', arguments['interface'],'down']) #ifcong eth0 down can be used as well
    subprocess.call(['ifconfig',arguments['interface'], 'hw', 'ether', arguments['mac_address']])
    subprocess.call(['ip', 'link', 'set', arguments['interface'],'up'])
    return 'Mac Address has been changed to ' + arguments['mac_address']

if __name__ == '__main__':
    inputs= get_arguments()
    notification= change_mac(inputs)
    print(notification)
