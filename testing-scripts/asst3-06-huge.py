#!/usr/bin/python

import core
import sys
import os

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing huge")
	test.set_timeout(300)
	test.send_command("p /testbin/huge")
	checks = ['stage \[1\] done', 'stage \[2\.0\] done', 'stage \[2\.1\] done', 'stage \[2\.2\] done', 'stage \[2\.3\] done', 'stage \[2\.4\] done', 'stage \[2\] done', 'You passed!']
		test.look_for_and_print_result(check.strip(), 1)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
