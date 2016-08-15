#!/usr/bin/python
from subprocess import check_output,call
from bs4 import BeautifulSoup
import sys

script, VM_NAME = sys.argv

# find the instance name using the VM name provided
retcode = call("nova --os-username=admin --os-project-name=admin --os-auth-url=http://10.250.117.53:5000/v2.0 --os-password=12f19b536fb94c91 list", shell=True)
if retcode == 0:
	INSTANCE_NAME = check_output("nova --os-username=admin --os-project-name=admin --os-auth-url=http://10.250.117.53:5000/v2.0 --os-password=12f19b536fb94c91 list --field instance_name,name | grep '%s' | awk '{print $4}'" %VM_NAME, shell=True).rstrip()
else:
	print("Couldn't get list of nova instances. Terminating...")
	sys.exit(1)

# check all the available virtual PCI devices avaialble
# we have only created 8 virtual functions
retcode = call("virsh nodedev-list --cap pci | grep 06", shell=True)
if retcode == 0:
	pci_devices_all = check_output("virsh nodedev-list --cap pci | grep 06", shell=True).split()
else:
	print("PCI device not found. Terminating...")
        sys.exit(1)

# remove the first item we get because that's the actual physical PCI device attached
pci_physical_device = pci_devices_all.pop(0)

# save the rest of the physical PCI devices in a new list
pci_virtual_devices = pci_devices_all

# need to detach the PCI device from the host first.
# if can't detach a device, that means that device is busy
# the first device we are able to detach from the host is the 
# one we will attach to the VM
for pci_device in pci_virtual_devices:
	retcode = call("sudo virsh nodedev-detach '%s'" %pci_device, shell=True)
	# if the above call is a success
	if retcode == 0:
		pci_device_free = pci_device
		break

#create a XML for the virtual function
pci_device_xml = check_output("virsh nodedev-dumpxml '%s'" %pci_device, shell=True)

#soupify the xml obtained to extract slot and function values
soup = BeautifulSoup(pci_device_xml,"lxml")
virtualFunction_slot = soup ('slot')[0].text
virtualFunction_function = soup ('function')[0].text
	
XML = "<hostdev mode=\"subsystem\" type=\"pci\" managed=\"yes\"> \
<source><address domain=\"0x0000\" bus=\"0x06\" slot=\"0x%s\" function=\"0x%s\" /> \
</source><address type=\"pci\" domain=\"0x0000\" bus=\"0x00\" slot=\"0x06\" function=\"0x0\" /></hostdev> " \
%(virtualFunction_slot, virtualFunction_function)
	
# create a xml file in the temp directory and save XML in it
try:
	with open ("/tmp/file.xml", "w") as outfile:
		outfile.write(XML)
except IOError:	
	print("XML file creation failed. Terminating...")
	sys.exit(1)

xml_file = "/tmp/file.xml"

# attach this XML file to the VM
retcode = call("sudo virsh attach-device '%s' '%s'" % (INSTANCE_NAME, xml_file), shell=True)
if retcode == 0:
	print("PCI devie %s successfully attached to VM %s" %(pci_device_free, VM_NAME))
else:
	print("Error attaching PCI device %s to VM %s" %(pci_device_free, VM_NAME))
	sys.exit(1)

