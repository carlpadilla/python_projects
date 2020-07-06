#!/bin/python3

# Syntax: python3 port_scanner.py <ip>

import sys
import socket
from datetime import datetime

# Define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translating hostname to ipv4
else:
    print('Invalid amount of arguments.')
    print('Syntax: python3 port_scanner.py <ip>')


print("_" * 50)
print('Scanning target ' + target)
print('Time started: ' + str(datetime.now()))
print("_" * 50)


try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))  # returns an error indicator
        # print('Checking port {}'.format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved')

except socket.error:
    print('Couldnt connect to server')
    sys.exit()
