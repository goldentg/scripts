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
    # Sort leases by IP address
    leases = sorted(leases, key=lambda x: x['ip'])
    return leases

leases = get_dhcp_leases()

workbook = xlsxwriter.Workbook('dhcp_leases.xlsx')
worksheet = workbook.add_worksheet()

# Define formatting for the header row
header_format = workbook.add_format({'bold': True, 'border': True, 'bg_color': '#D9D9D9'})

# Define formatting for the data rows
data_format = workbook.add_format({'border': True})

# Write the header row
worksheet.write(0, 0, 'IP', header_format)
worksheet.write(0, 1, 'Start', header_format)
worksheet.write(0, 2, 'End', header_format)
worksheet.write(0, 3, 'MAC', header_format)
worksheet.write(0, 4, 'Hostname', header_format)

# Write the data rows
row = 1
for lease in leases:
    worksheet.write(row, 0, lease.get('ip', ''), data_format)
    worksheet.write(row, 1, lease.get('start', ''), data_format)
    worksheet.write(row, 2, lease.get('end', ''), data_format)
    worksheet.write(row, 3, lease.get('mac', ''), data_format)
    worksheet.write(row, 4, lease.get('hostname', ''), data_format)
    row += 1

# Autofit the columns
worksheet.set_column(0, 0, 15)
worksheet.set_column(1, 2, 20)
worksheet.set_column(3, 4, 30)

# Close the workbook
workbook.close()

