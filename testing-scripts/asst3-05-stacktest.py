#!/usr/bin/python

import core
import sys
import os

def testPrintChar(kernel_name):
	global test
	stackfile = os.environ['TEST_PATH']
	test = core.TestUnit(kernel_name, "Testing stacktest")
	test.set_timeout(10)
	test.send_command("p /testbin/stacktest")
	f = open(stackfile + '/testing-files/stacktest.in', 'r')
	for check in f.readlines():
		test.look_for_and_print_result(check.strip(), 1)
	f.close()

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
