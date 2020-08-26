"""These script was to create to test against my CCNP Security lab.
   They are not intended for malicious use. If used to attack any system
   without authorization from that company/user means you are performing 
   an illegal act. Please act responsibly.""" 

import subprocess

interface= 'eth0'
mac_address= '00:11:22:33:44:55'

print('Changing the MAC Address for', interface, 'to', mac_address)
subprocess.call('ip link set ' +interface + ' down', shell= True) #ifcong eth0 down can be used as well
subprocess.call('ifconfig '+ interface + ' hw ether '+ mac_address, shell= True)
subprocess.call('ip link set '+ interface +' up', shell= True)
