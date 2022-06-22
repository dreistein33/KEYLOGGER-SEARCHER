import subprocess
import re

connections = subprocess.run(['netstat', '-ano'], capture_output=True).stdout.decode()
TCP = re.findall('TCP.+?(?=LISTENING)', connections)
IPv4_listener = '0.0.0.0:0'
IPv6_listener = '[::]:0'
potential_loggers = []

for items in TCP:
    listener_divider = items.split()
    fgn_address = listener_divider[2]
    if fgn_address == IPv4_listener or fgn_address == IPv6_listener:
        continue
    else:
        potential_loggers.append(items)

if len(potential_loggers) == 0:
    print('NO KEYLOGGERS FOUND, YOU\'RE SAFE :)')
else:
    for items in potential_loggers:
        print(f'KEYLOGGER FOUND AT:\n{items}')
