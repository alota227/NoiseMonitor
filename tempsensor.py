import time

while 1:
	tempfile = open("/sys/bus/w1/devices/28-5698031d64ff/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000
	print "{} C".format(temperature) 

	time.sleep(1)

