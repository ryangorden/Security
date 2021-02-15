import scapy.all as scapy
import argparse

def get_arguments():
    """
    Returns user inputs for interface and mac address
    :return: 
    """""
    # This class handle user input for us
    parser= argparse.ArgumentParser()
    parser.add_argument("-s", "--cidr", dest= "network", help= "Pleas enter host or network in cidr notation")

    # This separte the options from the value that follow them
    options= parser.parse_args()
    cidr= options.network
    if not cidr:
        parser.error("Please provide an network  in cidr noation. Use --help for more info")
    else:
        return options

def scan(ip):
    # This will allow us to create an ARP reqest ( who is x.x.x.x)
    arp_request= scapy.ARP(pdst=ip)

    # This section is creating a Ethernet frame that we can send
    # over the network. We are setting the destination mac in the
    # field.
    broadcast= scapy.Ether(dst= 'ff:ff:ff:ff:ff:ff')

    # This section will combine arp request with out Ethernet frame
    arp_request_broadcast= broadcast/arp_request

    # This nex section will allow us to send our ethernet frame
    answered_list= scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #
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
    ip =get_arguments().network
    targeted_clients= scan(ip)
    print_targeted_clients(targeted_clients)
