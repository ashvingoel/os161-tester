#!/usr/bin/python

import core
import sys

def testHelloWorld(path_to_kernel):
	kernel = core.TestUnit(path_to_kernel, "Testing Hello World")
	kernel.basic_read_test_and_print("Hello World")
	# kernel.send_command("q")

def main():
	path = str(sys.argv[1])
	testHelloWorld(path)

if __name__ == "__main__":
	main()
