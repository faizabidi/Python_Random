#!/usr/bin/python

from subprocess import call,check_output
import sys

# update the os
retcode = call("sudo yum update -y", shell=True)
if retcode == 1:
	print("Couldn't update the OS. Terminating...")
	sys.exit(1)

# check the kernel version you have
kernel_version = check_output("uname -r", shell=True)

# install necessary packages
retcode = call("sudo yum install perl createrepo python-devel \
	pciutils lsof redhat-rpm-config rpm-build gcc gtk2 atk \
	cairo gcc-gfortran tcsh libnl tcl tk wget 'kernel-devel-uname-r == %s' -y" %(kernel_version), shell=True)
if retcode == 1:
	print("Couldn't install all the needed packages. Terminating....")
	sys.exit(1)


# the symbolic link of /usr/src/kernels/your-version/ would be broken probably. Need do fix that. 
kernel_version = kernel_version.rstrip ('\n')

# go to /lib/modules/your-version and delete the "build" folder
retcode = call("sudo rm -r /lib/modules/'%s'/build" %kernel_version, shell=True)
if retcode == 1:
	print("Couldn't delete the build folder. Terminating...")
	sys.exit(1)
else:
	print("Removed build folder. Creating a symlink now....")

# fix the symbolic link
retocde = call("cd /lib/modules/'%s' && sudo ln -s /usr/src/kernels/'%s' build" % (kernel_version, kernel_version), shell=True)
if retcode == 1:
	print("Couldn't fix the symlink. Terminating...")
	sys.exit(1)


# download Mellanox driver for Centos 7.2 if not already there
retcode = call("ls | grep MLNX", shell=True)
if retcode == 1:
	print("Downloading the Mellanox drivers.....")
	retcode2 = call("wget http://www.mellanox.com/downloads/ofed/MLNX_OFED-3.3-1.0.4.0/MLNX_OFED_LINUX-3.3-1.0.4.0-rhel7.2-x86_64.tgz", shell=True)
	if retcode2 == 1:
		print("Couldn't download the Mellanox drivers. Terminating...")
		sys.exit(1)

# untar the Mellanox driver
call("tar -xf MLNX_OFED_LINUX-3.3-1.0.4.0-rhel7.2-x86_64.tgz", shell=True)

# navigate to the Mellanox driver folder, and install it
retcode =  call("cd MLNX_OFED_LINUX-3.3-1.0.4.0-rhel7.2-x86_64 && sudo ./mlnxofedinstall --add-kernel-support", shell=True)
if retcode == 0:
	print "Successfully installed Mellanox driver"
else:
	print "Mellanox driver installation failed. Terminating..."

# restart the driver
retcode = call("sudo /etc/init.d/openibd restart", shell=True)  
if retcode == 1:
	print("Couldn't restart the Mellanox driver. Terminating...")
	sys.exit(1)

