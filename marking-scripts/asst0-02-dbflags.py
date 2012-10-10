#!/usr/bin/python

import core
import sys

def checkDBValue(res):
	check = 'Current value of dbflags is ' + res
	test.send_command("dbflags")
	return test.look_for_and_return_mark(check, 1)

def setDBValue(value, on):
	path = "df " + value + " " + on
	test.send_command(path)

def failDBValue(value, on):
	print "Turning " + on + " dbflags value " + str(value)
	check = 'Usage: df nr on\/off'
	setDBValue(value, on)
	return test.look_for_and_return_mark(check, 1)

def testDBValue(value, on, res):
	print "Turning " + on + " dbflags value " + str(value)
	setDBValue(str(value), on)
	return checkDBValue(res)

def testDBFlags(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing dbflags", True)
	#Check if we have the dbflags menu option
	test.send_command("?o")
	return test.look_for_and_return_mark('\[dbflags\] Debug flags', 1)

def main():
	mark = 0
	on = "on"
	off = "off"
	path = str(sys.argv[1])
	mark += testDBFlags(path)
	mark += checkDBValue("0x0")
	mark += testDBValue(1, on, "0x1")
	mark += testDBValue(1, off, "0x0")
	mark += testDBValue(5, on, "0x10")
	mark += failDBValue(str(13), on)
	mark += testDBValue(8, on, "0x90")
	mark += testDBValue(3, off,"0x90")
	mark += testDBValue(3, on, "0x94")
	mark += testDBValue(11, on, "0x494")
	mark += failDBValue(str(23), on)
	mark += testDBValue(11, off, "0x94")
	mark += testDBValue(8, off, "0x14")
	mark += testDBValue(5, off, "0x4")
	mark += testDBValue(3, off, "0x0")
	mark += testDBValue(str(45), off)
	
	test.clean_kernel()

	print mark



if __name__ == "__main__":
	main()
