#!/usr/bin/python

import core
import sys

def main():
	test = core.TestUnit("multiply")
	test.runprogram("/testbin/multiply", "3 5")
	check = '15'
	test.look_for_and_print_result(check, 4)

if __name__ == "__main__":
	main()
