#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing triplesort")
	test.set_timeout(120)
	check = 'sort: Passed'
	for i in range(3):
		test.look_for_and_print_result(check, 5)
	#We should have finished everything by now, so let's just reduce the timeout
	test.set_timeout(10)
	check = 'Congratulations! You passed'
	test.look_for_and_print_result(check, 5)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
