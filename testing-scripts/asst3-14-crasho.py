#!/usr/bin/python

import core
import sys

def test(kernel_name):
	test = core.TestUnit(kernel_name, "crash test o")
	test.set_timeout(180)
        test.send_command("p /testbin/crash o")
        test.look_for_and_print_result('\nFatal user mode trap 3', 10)

def main():
	path = str(sys.argv[1])
	test(path)

if __name__ == "__main__":
	main()
