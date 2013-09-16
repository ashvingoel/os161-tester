#!/usr/bin/python

import core
import sys

def main():
	test = core.TestUnit("waitexit4")
        test.runprogram("/testbin/waitexit4")
	check = 'att'
	test.look_for_and_print_result(check, 5)

if __name__ == "__main__":
	main()
