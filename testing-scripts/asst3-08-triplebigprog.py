#!/usr/bin/python

import core
import sys

def test(kernel_name):
	test = core.TestUnit(kernel_name, "triplebigprog test")
        test.send_command("p /testbin/triplebigprog")
        test.look_for_and_print_result('\n/testbin/triplebigprog: Congratulations! You passed.', 20)

def main():
	path = str(sys.argv[1])
	test(path)

if __name__ == "__main__":
	main()
