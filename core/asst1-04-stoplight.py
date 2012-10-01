#!/usr/bin/python

import core
import sys

def stoplight(test):
        result = 0
	test.send_command('1c')
        i = 0

        while True:
            out = test.look_for( \
                ['approaching: car =\s+(\d), direction = ([NSEW]), destination = ([NSEW])', \
                     'region1:     car =\s+(\d), direction = ([NSEW]), destination = ([NSEW])', \
                     'region2:     car =\s+(\d), direction = ([NSEW]), destination = ([NSEW])', \
                     'region3:     car =\s+(\d), direction = ([NSEW]), destination = ([NSEW])', \
                     'leaving:     car =\s+(\d), direction = ([NSEW]), destination = ([NSEW])', \
                     'Operation took'])
            if out < 0:
                result = -1 # no match failure
                break

            if out == 5: # end of program
                break

            i = i + 1

            nr, direction, destination = test.kernel().match.groups()
            nr = int(nr)
        return result

def main():
	kernel_name = str(sys.argv[1])
	test = core.TestUnit(kernel_name, "Testing stoplight")
        result = stoplight(test)
        test.print_result(result)

if __name__ == "__main__":
	main()
