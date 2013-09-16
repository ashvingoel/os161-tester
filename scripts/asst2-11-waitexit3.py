#!/usr/bin/python

import core
import sys

def main():
	test = core.TestUnit("waitexit3")
        test.runprogram("/testbin/waitexit3")
	check = 'acp'
	test.look_for_and_print_result(check, 6)

if __name__ == "__main__":
	main()
