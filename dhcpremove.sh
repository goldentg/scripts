#!/bin/bash

# Prompt the user to enter the IPv4 address to be removed from the DHCP server
echo "Enter the IPv4 address to be removed from the DHCP server:"
read ip_address

# Remove the IPv4 address from the DHCP server using the dhcp-lease-list command and awk
dhcp-lease-list | awk '$3 == ip_address { print $2 }' | xargs -I {} sudo dhcp-lease-remove {}

# Display a message to confirm that the IPv4 address has been removed from the DHCP server
echo "The IPv4 address $ip_address has been removed from the DHCP server."
