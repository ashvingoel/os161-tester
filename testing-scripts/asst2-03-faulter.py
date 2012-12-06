#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("Testing faulter")
    check = 'Entering the faulter program - I should die immediately'
    test.runprogram("/testbin/faulter")
    test.look_for_and_print_result(check, 7)

if __name__ == "__main__":
	main()
