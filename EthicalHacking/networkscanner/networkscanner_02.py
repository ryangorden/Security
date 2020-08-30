import scapy.all as scapy
import sys

def scan(ip):
    arp_request= scapy.ARP(pdst=ip)
    broadcast= scapy.Ether(dst= 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast= broadcast/arp_request
    #scapy.ls(scapy.ARP()) # this will list what fields we have to work with in the APR() class.
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    targeted_clients= list()
    for element in answered_list:
        client= {'mac': element[1].hwsrc, 'ip': element[1].psrc}
        targeted_clients.append(client)
    
    return targeted_clients

def print_targeted_clients(target_clients):
    print('\nScanned IP Address          Scanned Mac Address')
    print('\n------------------          -------------------')
    
    for client in targeted_clients:
        print('\n{:10}                  {:10}'.format(client['ip'], client['mac']))
    
if __name__=='__main__':
    targeted_clients= scan(sys.argv[1])
    print_targeted_clients(targeted_clients)
