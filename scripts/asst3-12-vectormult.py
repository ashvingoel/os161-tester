#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("vectormult")
    test.runprogram("/testbin/vectormult")
    test.look_for_and_print_result('\nPassed.', 25)

if __name__ == "__main__":
	main()
