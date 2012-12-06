#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("bigprog")
    test.runprogram("/testbin/bigprog")
    test.look_for_and_print_result('\nPassed bigprog test.', 10)

if __name__ == "__main__":
	main()
