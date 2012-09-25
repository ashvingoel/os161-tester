#!/usr/bin/python

import core
import sys

def testPrintChar(path_to_kernel):
	global kernel
	kernel = core.TestUnit(path_to_kernel, "Testing printchar")
	# check = 'H*e*l*l*o*w*o*r*l*d*\!*H*e*l*l*o*p*r*i*n*t*f*\!*'
	check = 'H.*e.*l.*l.*o.*w.*o.*r.*l.*d.*\!.*H.*e.*l.*l.*o.*p.*r.*i.*n.*t.*f.*\!'
	#check = 'H*e*l*l*o*p*r*i*n*t*f*\!'
	#check = 'H**e**l**l**o**p**r**i**n**t**f**\!'
	kernel.send_command("p /testbin/printchar")
	out = kernel.basic_read_test(check)
	if out is True:
		print "PASS"
	else:
		print "FAIL"


def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()