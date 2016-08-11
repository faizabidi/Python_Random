#!/usr/bin/python
from subprocess import check_output,call
from bs4 import BeautifulSoup
from sys import argv

script, VM_NAME = argv

# find the instance name using the VM name provided

INSTANCE_NAME = check_output("nova list --field instance_name,name | grep '%s' | awk '{print $4}'" %VM_NAME, shell=True).rstrip()

#check all the available virtual PCI devices avaialble
#we have only created 8 virtual functions
pci_devices_all = check_output("virsh nodedev-list --cap pci | grep 06", shell=True).split ()

#remove the first item we get because that's the actual physical PCI device attached
pci_physical_device = pci_devices_all.pop(0)

#save the rest of the physical PCI devices in a new list
pci_virtual_devices = pci_devices_all

#need to detach the PCI device from the host first.
#if can't detach a device, that means that device is busy
#the first device we are able to detach from the host is the 
#one we will attach to the VM
for pci_device in pci_virtual_devices:
	retcode = call("sudo virsh nodedev-detach '%s'" %pci_device, shell=True)
	#out = subprocess.check_output()
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
	
#create a xml file in the temp directory and save XML in it
new_file = open ("/tmp/file.xml", "w")
new_file.write (XML)
new_file.close ()
xml_file = "/tmp/file.xml"

#attach this XML file to the VM
print  (INSTANCE_NAME, xml_file)
call("sudo virsh attach-device '%s' '%s'" % (INSTANCE_NAME, xml_file), shell=True)

