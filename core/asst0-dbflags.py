#!/usr/bin/python

import core
import sys

def checkDBValue(res):
	check = 'Current value of dbflags is ' + res
	kernel.send_command("dbflags")
	out = kernel.basic_read_test(check)
	if out is True:
		print "PASS"
	else:
		print "FAIL"


def setDBValue(value, on):
	path = "df " + str(value) + " " + on
	kernel.send_command(path)

def testDBValue(value, on, res):
	setDBValue(value, on)
	return checkDBValue(res)

def testDBFlags(path_to_kernel):
	global kernel
	kernel = core.TestUnit(path_to_kernel)
	#Check if we have the dbflags menu option
	kernel.send_command("?o")
	res = kernel.basic_read_test('\[dbflags\] Debug flags')
	#res = kernel.basic_test_unit("?o", '\[dbflags\] Debug flags')
	if res is True:
		print "PASS"
	else:
		print "FAIL"


def main():
	on = "on"
	off = "off"
	path = str(sys.argv[1])
	testDBFlags(path)
	checkDBValue("0x0")
	testDBValue(1, on, "0x1")



if __name__ == "__main__":
	main()
