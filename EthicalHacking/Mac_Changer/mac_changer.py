"""These script was to create to test against my CCNP Security lab.
   They are not intended for malicious use. If used to attack any system
   without authorization from that company/user means you are performing
   an illegal act. Please act responsibly."""

import subprocess
import optparse
import re

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
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])

def get_current_mac(interface, mac_address):
    """
    This function will check to see did the mac address change
    for the interface
    :return:
    """
    ifconfig= subprocess.check_output(["ifconfig", interface])
    mac_address_result= re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig.decode("utf-8"))

    if mac_address_result:
        if (mac_address_result.group(0)) == mac_address:
            return ("Mac was change successfully: "+ mac_address_result.group(0))
        else:
            return ("Mac did not change: " + mac_address_result.group(0))
    else:
        return "No mac found"



if __name__ == "__main__":
    interface=get_arguments().interface
    mac_address= get_arguments().new_mac
    mac=mac_changer(interface,mac_address)
    macAdress= get_current_mac(interface, mac_address)
    print(macAdress)