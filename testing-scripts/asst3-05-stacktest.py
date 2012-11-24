#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing stacktest")
	test.set_timeout(10)
	test.send_command("p /testbin/stacktest")
	f = open('stacktest.in', 'r')
	for check in f.readlines():
		print check
		test.look_for_and_print_result(check, 1)
	f.close()

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
