#!/usr/bin/python

import core
import sys

def testHelloWorld(kernel_name):
	test = core.TestUnit(kernel_name, "Testing Hello World", True)
	mark = test.look_for_and_return_mark("Hello World", 5)
	print "Hello world test mark is " + str(mark)
	test.clean_kernel()
        # why do we need to send the quit command? -Ashvin
	# test.send_command("q")

def main():
	path = str(sys.argv[1])
	testHelloWorld(path)

if __name__ == "__main__":
	main()
