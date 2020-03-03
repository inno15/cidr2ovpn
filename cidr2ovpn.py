from netaddr import *
import sys

filepath = './subnetlistfile.txt'
subnet_file = open(filepath,'r')
while True:
	try:
		subnet = subnet_file.readline()
		subnet = subnet.rstrip("\n")
		network = IPNetwork(subnet)
		sys.stdout.write("route " + str(network.ip) + " " + str(network.netmask) + "\n")
	except AddrFormatError:
		print ("Done")
		exit()

