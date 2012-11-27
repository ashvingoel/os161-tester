#!/usr/bin/python

import core
import sys

def test(kernel_name):
	test = core.TestUnit(kernel_name, "bigprog test")
        test.send_command("p /testbin/bigprog")
        test.look_for_and_print_result('\nPassed bigprog test.', 10)

def main():
	path = str(sys.argv[1])
	test(path)

if __name__ == "__main__":
	main()
