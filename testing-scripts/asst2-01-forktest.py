#!/usr/bin/python

import core
import sys

def testForkTest(kernel_name):
	global test
	test = core.TestUnit(kernel_name, "Testing forktest")
	check = '001111222222223333333333333333'
	test.send_command("p /testbin/forktest")
	test.look_for_and_print_result(check)

def main():
	path = str(sys.argv[1])
	testForkTest(path)



if __name__ == "__main__":
	main()
