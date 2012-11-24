#!/usr/bin/python

import core
import sys

def testPrintChar(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing triplemat")
	test.set_timeout(600)
	check = 'answer is: 82313733 \(should be 8772192\)'
	test.send_command("p /testbin/triplemat")
	for i in range(3):
		test.look_for_and_print_result(check, 5)
	check = 'testbin/triplemat: Congratulations! You passed.'
	test.look_for_and_print_result(check, 5)

def main():
	path = str(sys.argv[1])
	testPrintChar(path)


if __name__ == "__main__":
	main()
