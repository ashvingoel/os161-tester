#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing use of wait and exit V")
	check1 = 'we'
	check2 = 'Invalid argument'
	test.send_command("p /testbin/waitexit5")
	test.look_for_and_print_result(check1, 4)
	test.look_for_and_print_result(check2, 4)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)



if __name__ == "__main__":
	main()
