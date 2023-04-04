import os
import xlsxwriter

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

workbook = xlsxwriter.Workbook('dhcp_leases.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

worksheet.write(row, col, 'IP')
worksheet.write(row, col + 1, 'Start')
worksheet.write(row, col + 2, 'End')
worksheet.write(row, col + 3, 'MAC')
worksheet.write(row, col + 4, 'Hostname')

row += 1

for lease in leases:
    worksheet.write(row, col , lease.get('ip', ''))
    worksheet.write(row, col + 1 , lease.get('start', ''))
    worksheet.write(row,col + 2 , lease.get('end', '')) 
    worksheet.write(row,col + 3 , lease.get('mac', '')) 
    worksheet.write(row,col + 4 , lease.get('hostname', '')) 
    row += 1

workbook.close()
