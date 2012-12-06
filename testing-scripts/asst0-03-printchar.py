#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("printchar")
    test.runprogram("/testbin/printchar")
    check = 'H.*e.*l.*l.*o.*w.*o.*r.*l.*d.*\!.*H.*e.*l.*l.*o.*p.*r.*i.*n.*t.*f.*\!'
    test.look_for_and_print_result(check, 10)

if __name__ == "__main__":
    main()
