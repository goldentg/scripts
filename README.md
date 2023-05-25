This repo is a collection of scripts I have written to manage Ubuntu Server services for my home lab. 

| Script | Purpose | Usage |
|-------|--------|--------|
| dhcp_leases.py | Prints DHCP lease table to terminal | sudo python3 dhcp_leases.py |
| dhcp_excel_v2.py | creates an excel spreadsheet with lease information | sudo python3 dhcp_excel_v2.py |
| dhcp_excel.py | Same function as v2, just less refined | sudo python3 dhcp_excel.py |
| dhcpremove.sh | Removes a dhcp lease using an IPv4 address | sudo ./dhcpremove.sh |
| dhcpreserve.py | Adds a reservation using IPv4 and MAC addresses | sudo python3 dhcpreserve.py |
| openvpnTimer.sh | Prevents OpenVPN service from downtime. This works by pinging Google DNS (8.8.8.8) in a predetermined interval. If the system is not facing an internet issue, and there is an issue with the OpenVPN daemon, the system will restart. Although this is not the most efficient way of doing this, it is effective and useful in some use cases | There are many ways to implement this. It does take some know-how to implement but the idea is to make this script run on startup |