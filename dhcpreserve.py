#!/usr/bin/env python3

import subprocess

# Get user input for IP address and MAC address
ip_address = input("Enter IPv4 address to reserve: ")
mac_address = input("Enter MAC address to reserve: ")

# Define the dhcpd.conf file path
dhcpd_conf_file = "/etc/dhcp/dhcpd.conf"

# Define the dhcpd.leases file path
dhcpd_leases_file = "/var/lib/dhcp/dhcpd.leases"

# Check if the IP address is already reserved
reserved_ip = subprocess.getoutput("grep {} {}".format(ip_address, dhcpd_leases_file))

if reserved_ip:
    print("IP address already reserved!")
else:
    # Add reservation to the dhcpd.conf file
    with open(dhcpd_conf_file, "a") as f:
        f.write("host reserved_host { \n")
        f.write("  hardware ethernet " + mac_address + ";\n")
        f.write("  fixed-address " + ip_address + ";\n")
        f.write("}\n")

    # Restart the dhcp server
    subprocess.run(["systemctl", "restart", "isc-dhcp-server.service"])

    print("IP address {} reserved for MAC address {}".format(ip_address, mac_address))
