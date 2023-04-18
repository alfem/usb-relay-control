#!/usr/bin/python
# Control USB relays board from CFsunbird
# Author: Alfonso de Cala <alfonso@el-magnifico.org>

DEVICE='/dev/hidraw1'

prefix=int('A1',16)
relay=1
command=0
checksum=prefix+relay+command

buffer=bytearray([prefix,relay,command,checksum])

with open(DEVICE, 'wb') as f:
  f.write(buffer)

  

