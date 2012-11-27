#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing triplemat")
	test.set_timeout(240)
	test.send_command("p /testbin/triplemat")
        test.look_for_and_print_result('\n/testbin/triplemat: Congratulations! You passed.', 20)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
