#!/usr/bin/python

import core
import sys

def main():
	test = core.TestUnit("waitexit5")
        test.runprogram("/testbin/waitexit5")
	check1 = 'we'
	check2 = 'Invalid argument'
	test.look_for_and_print_result_no_wait(check1, 2)
	test.look_for_and_print_result(check2, 5)

if __name__ == "__main__":
	main()
