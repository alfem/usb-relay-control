#!/usr/bin/python
# Control USB relays board from CFsunbird
# Author: Alfonso de Cala <alfonso@el-magnifico.org>

# Device file name usually is /dev/hidrawN
# Your user should have write permission to this file (or run the script as root)

import sys

# Get parameters from command line
if len(sys.argv) != 4:
    print("Usage: python usb-relay.py <device file name> <relay number> <on/off>")
    sys.exit(1)

DEVICE = sys.argv[1]
RELAY = int(sys.argv[2])
COMMAND = sys.argv[3]

# Parameter checking
if RELAY < 1 or RELAY > 4:
    print("Relay number must be between 1 and 4")
    sys.exit(1)

if COMMAND == "on":
  command = 0
elif COMMAND == "off":
   command = 1
else:   
    print("Command must be 'on' or 'off'")
    sys.exit(1)

prefix=int('A1',16)
relay=int(RELAY)
checksum=prefix+relay+command

buffer=bytearray([prefix,RELAY,command,checksum])

with open(DEVICE, 'wb') as f:
  f.write(buffer)

  

