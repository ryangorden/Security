import subprocess

interface= 'eth0'
mac_address= '00:11:22:33:44:55'

print('Changing the MAC Address for', interface, 'to', mac_address)
subprocess.call('ip link set ' +interface + ' down', shell= True) #ifcong eth0 down can be used as well
subprocess.call('ifconfig '+ interface + ' hw ether '+ mac_address, shell= True)
subprocess.call('ip link set '+ interface +' up', shell= True)
