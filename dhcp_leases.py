import os

def get_dhcp_leases():
    leases = []
    with open('/var/lib/dhcp/dhcpd.leases', 'r') as f:
        for line in f:
            if line.startswith('lease'):
                lease = {}
                lease['ip'] = line.split()[1]
            elif line.strip().startswith('starts'):
                lease['start'] = ' '.join(line.split()[2:4]).replace(';','')
            elif line.strip().startswith('ends'):
                lease['end'] = ' '.join(line.split()[2:4]).replace(';','')
            elif line.strip().startswith('hardware ethernet'):
                lease['mac'] = line.split()[2].replace(';','')
            elif line.strip().startswith('client-hostname'):
                lease['hostname'] = line.split()[1].replace(';','').replace('"', '')
            elif line.strip() == '}':
                leases.append(lease)
    return leases

leases = get_dhcp_leases()
for lease in leases:
    print(lease)
