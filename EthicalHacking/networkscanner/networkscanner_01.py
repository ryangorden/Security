import scapy.all as scapy



def scan(ip):
    """
    this function takes a host ip address or
    subnet and does a network scan at L2.
    """
    scapy.arping(ip)


if __name__=='__main__':
    scan('192.168.86.1/24')
