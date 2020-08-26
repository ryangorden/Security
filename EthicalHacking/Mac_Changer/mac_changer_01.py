"""These script was to create to test against my CCNP Security lab.
   They are not intended for malicious use. If used to attack any system
   without authorization from that company/user means you are performing 
   an illegal act. Please act responsibly.""" 

import subprocess

try:
    interface= input('Enter name of Interface: ')
    mac_address= input('What do you want your mac address to be: ')
except:
    interface= raw_input('Enter name of Interface: ')
    mac_address= raw_input('What do you want your mac address to be: ')


print('Changing the MAC Address for', interface, 'to', mac_address)
#subprocess.call('ip link set ' +interface + ' down', shell= True) #ifcong eth0 down can be used as well
#subprocess.call('ifconfig '+ interface + ' hw ether '+ mac_address, shell= True)
#subprocess.call('ip link set '+ interface +' up', shell= True)

subprocess.call(['ip', 'link', 'set', interface,'down']) #ifcong eth0 down can be used as well
subprocess.call(['ifconfig', interface, 'hw', 'ether', mac_address])
subprocess.call(['ip', 'link', 'set', interface,'up'])
