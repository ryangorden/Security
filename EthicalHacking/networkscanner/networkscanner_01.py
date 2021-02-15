import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)


if __name__=='__main__':
    scan('192.168.86.1/24')
