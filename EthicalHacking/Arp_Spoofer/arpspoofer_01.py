import scapy.all as scapy

# First field I am going to set is the op field.
# Set to 1 by default which mean when you create
# an arp packet you will create an arpp request.
# We will set it to 2 which will change it to a
# response.
packet= scapy.ARP(op=2, pdst="10.0.2.15", hwdst= "08:00:27:e6:e5:59", psrc= "10.0.2.1")

print("==================================================")
print("                   DETAILS")
print("==================================================")
print(packet.show)
print("\n")
print("==================================================")
print("                   SUMMARY")
print("==================================================")
print(packet.summay)
