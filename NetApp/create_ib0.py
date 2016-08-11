#!/usr/bin/python
from subprocess import check_output,call
from sys import argv

script, IP_ADDR = argv 

# create ib0 structure
ib0 = '''ONBOOT=yes
Name=ib0
DEVICE=ib0
Type=InfiniBand
IPADDR=%s
PREFIX=24
DEFROUTE=no
NM_CONTROLLED=no''' %IP_ADDR

# save it in a file and move it to the right location
new_file = open("ifcfg-ib0", "w")
new_file.write(ib0)
new_file.close()

# activate ib0
call("sudo mv ifcfg-ib0 /etc/sysconfig/network-scripts && sudo ifup ib0", shell=True)

