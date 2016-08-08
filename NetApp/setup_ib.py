#!/usr/bin/python

from subprocess import call,check_output

#update the os
call("sudo yum update -y", shell=True)

#check the kernel version you have
kernel_version = check_output ("uname -r", shell=True)

#install necessary packages
call ("sudo yum install perl createrepo python-devel \
	pciutils lsof redhat-rpm-config rpm-build gcc gtk2 atk \
	cairo gcc-gfortran tcsh libnl tcl tk wget 'kernel-devel-uname-r == %s' -y" %(kernel_version), shell=True)

#the symbolic link of /usr/src/kernels/your-version/ would be broken probably. Need do fix that. 
kernel_version = kernel_version.rstrip ('\n')

#go to /lib/modules/your-version and delete the "build" folder
call ("sudo rm -r /lib/modules/'%s'/build" %kernel_version, shell=True)
print "Removed build folder. Creating a symlink now....\n"

#fix the symbolic link
call ("cd /lib/modules/'%s' && sudo ln -s /usr/src/kernels/'%s' build" % (kernel_version, kernel_version), shell=True)

#download Mellanox driver for Centos 7.2 if not already there
retcode = call ("ls | grep MLNX", shell=True)
if retcode != 0:
	print "Downloading the Mellanox drivers.....\n"
	call ("wget http://www.mellanox.com/downloads/ofed/MLNX_OFED-3.3-1.0.4.0/MLNX_OFED_LINUX-3.3-1.0.4.0-rhel7.2-x86_64.tgz", shell=True)

#untar the Mellanox driver
call ("tar -xf MLNX_OFED_LINUX-3.3-1.0.4.0-rhel7.2-x86_64.tgz", shell=True)

#navigate to the Mellanox driver folder, and install it
retcode =  call ("cd MLNX_OFED_LINUX-3.3-1.0.4.0-rhel7.2-x86_64 && sudo ./mlnxofedinstall --add-kernel-support", shell=True)
if retcode == 0:
	print "Successfully installed Mellanox driver"
else:
	print "Mellanox driver installation failed."

#restart the driver
call ("sudo /etc/init.d/openibd restart", shell=True)  
 
