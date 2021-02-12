import subprocess
import optparse
import sys

def get_arguments():
    """
    Returns user inputs for interface and mac address
    :return: 
    """""
    # This class handle user input for us
    parser= optparse.OptionParser()
    parser.add_option("-i", "--interface", dest= "interface", help= "Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest= "new_mac", help= "New MAC Address")

    # This separte the options from the value that follow them
    # ex python mac_changer -i wlan0 -m aa:bb:cc:ee:ff:22
    (options, arguments)= parser.parse_args()
    interface= options.interface
    mac_addrss= options.new_mac
    if not interface:
        parser.error("Please provide an interface. Use --help for more info")
    elif not mac_addrss:
        parser.error("Please provide a mac address. Use --help for more info")
    else:
        return options
        #return {"interface":interface, "new_mac": mac_addrss}

def change_mac_unsecure(interface,mac_address):
    """
    This function will change the mac address of your interface
    for a linux device.
    :param interface:
    :param mac_address:
    :return:
    """
    print("Changing mac address for " + interface + " to " + mac_address)
    subprocess.call("ifconfig", shell=True)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + mac_address, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    return subprocess.call("ifconfig", shell=True)

def mac_changer(interface, mac_address):
    """
    This function will change the mac address of your interface
    for a linux device.
    :param interface:
    :param mac_address:
    :return:
    """
    subprocess.call(["ifconfig"])
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call("ifconfig",interface,"hw ether",mac_address])
    subprocess.call(["ifconfig",nterface,"up"])
    return subprocess.call(["ifconfig"])

if __name__ == "__main__":
    interface=get_arguments().interface
    mac_address= get_arguments().new_mac
    print(mac_address)
    print(interface)
    # mac=change_mac_unsecure(interface,mac_address)
    # print(mac)

