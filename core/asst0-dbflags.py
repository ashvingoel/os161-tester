#!/usr/bin/python

import core
import sys

def checkDBValue(res):
	check = 'Current value of dbflags is ' + res
	kernel.send_command("dbflags")
	kernel.basic_read_test_and_print(check)

def setDBValue(value, on):
	path = "df " + str(value) + " " + on
	kernel.send_command(path)

def failDBValue(value, on):
	print "Turning " + on + " dbflags value " + str(value)
	check = 'Usage: df nr on\/off'
	setDBValue(value, on)
	kernel.basic_read_test_and_print(check)

def testDBValue(value, on, res):
	print "Turning " + on + " dbflags value " + str(value)
	setDBValue(value, on)
	return checkDBValue(res)

def testDBFlags(path_to_kernel):
	global kernel
	kernel = core.TestUnit(path_to_kernel, "Testing dbflags")
	#Check if we have the dbflags menu option
	kernel.send_command("?o")
	kernel.basic_read_test_and_print('\[dbflags\] Debug flags')

def main():
	on = "on"
	off = "off"
	path = str(sys.argv[1])
	testDBFlags(path)
	checkDBValue("0x0")
	testDBValue(1, on, "0x1")
	testDBValue(1, off, "0x0")
	testDBValue(5, on, "0x10")
	failDBValue(13, on)



if __name__ == "__main__":
	main()
