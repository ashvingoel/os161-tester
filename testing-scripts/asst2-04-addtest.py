#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("add")
    test.runprogram("/testbin/add", "2 3")
    check = 'Answer: 5'
    test.look_for_and_print_result(check, 5)

if __name__ == "__main__":
	main()
