#!/usr/bin/python
from subprocess import check_output,call
import sys

script, IP_ADDR, NETMASK = sys.argv 

# create ib0 structure
ib0 = '''ONBOOT=yes
Name=ib0
DEVICE=ib0
Type=InfiniBand
IPADDR=%s
NETMASK=%s
DEFROUTE=no
NM_CONTROLLED=no''' %(IP_ADDR,NETMASK)

# save it in a file and move it to the right location
try:
	with open("ifcfg-ib0", "w") as outfile:
		outfile.write(ib0)
except IOError:
	print("ifcfg-ib0 couldn't be created. Terminating...")
	sys.exit(1)

# activate ib0
retcode = call("sudo mv ifcfg-ib0 /etc/sysconfig/network-scripts && sudo /usr/sbin/ifup ib0", shell=True)
if retcode == 1:
	print ("Error activating ib0")
        sys.exit(1)
else:
	print("Successfully activated ib0. Try pinging 192.168.1.100 to confirm.")

