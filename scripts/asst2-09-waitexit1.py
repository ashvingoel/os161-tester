#!/usr/bin/python

import core
import sys

def main():
	test = core.TestUnit("waitexit1")
        test.runprogram("/testbin/waitexit1")
	check = 'wekp'
	test.look_for_and_print_result(check, 6)

if __name__ == "__main__":
	main()
