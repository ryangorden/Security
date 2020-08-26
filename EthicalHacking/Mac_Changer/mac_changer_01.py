"""These script was to create to test against my CCNP Security lab.
   They are not intended for malicious use. If used to attack any system
   without authorization from that company/user means you are performing 
   an illegal act. Please act responsibly.""" 

import subprocess
import sys
import re

def get_arguments():
    arguments= {
                'interface': sys.argv[1],
                'mac_address': sys.argv[2]
               }
    return arguments

def change_mac(arguments):
    print('Changing the MAC Address for ' + arguments['interface']+ ' to '+ arguments['mac_address'])
    subprocess.call(['ip', 'link', 'set', arguments['interface'],'down']) #ifcong eth0 down can be used as well
    subprocess.call(['ifconfig',arguments['interface'], 'hw', 'ether', arguments['mac_address']])
    subprocess.call(['ip', 'link', 'set', arguments['interface'],'up'])

def validate_mac_change(arguments):
    print('Validating the Mac address has changed to '+ arguments['mac_address'])
    interface= subprocess.check_output(['ip', 'link', 'show', arguments['interface']])
    interfacetext= interface
    try:
        mactxt= re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', interfacetext)
        if mactxt.group(0)== arguments['mac_address']:
            print('Mac Address has been changed to ' + arguments['mac_address'])
        else:
            print('The mac address was not changed.')
    except:
        mactxt= re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', interfacetext.decode('utf8'))
        if mactxt.group(0)== arguments['mac_address']:
            print('Mac Address has been changed to ' + arguments['mac_address'])
        else:
            print('The mac address was not changed.')



if __name__ == '__main__':
    inputs= get_arguments()
    change_mac(inputs)
    validate_mac_change(inputs)
