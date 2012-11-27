#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing matmult")
	test.set_timeout(60)
	test.send_command("p /testbin/matmult")
        test.look_for_and_print_result('\nPassed.', 10)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
