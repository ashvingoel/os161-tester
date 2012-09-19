#!/usr/bin/python

import core
import sys

def testHelloWorld(path_to_kernel):
	kernel = core.TestUnit(path_to_kernel)
	ret = kernel.basic_read_test("Hello World")
	kernel.send_command("q")
	return ret

def main():
	path = str(sys.argv[1])
	a = testHelloWorld(path)
	if a is True:
		print "PASS"
	else:
		print "FAIL"

if __name__ == "__main__":
	main()
