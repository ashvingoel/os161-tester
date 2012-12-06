#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("palin")
    test.runprogram("/testbin/palin")
    check = 'IS a palindrome'
    test.look_for_and_print_result(check, 4)

if __name__ == "__main__":
	main()
