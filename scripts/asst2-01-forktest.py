#!/usr/bin/python

import core
import sys

def main():
    test = core.TestUnit("forktest")
    test.runprogram("/testbin/forktest")

    # when we fix forktest, this is all we need to look for
    # check = '001111222222223333333333333333'
    # test.look_for_and_print_result(check, 20)

    out = test.look_for("([0123]{30,30})$")
    if out < 0:
        test.print_result(0, 10)
        return

    output = test.kernel.match.group(0)
    output_array = [0] * 4
    for i in range(len(output)):
        index = int(output[i])
        output_array[index] = output_array[index] + 1
    if (output_array[0] == 2) and (output_array[1] == 4) and \
            (output_array[2] == 8) and (output_array[3] == 16):
        test.print_result(10, 10)
    else:
        test.print_result(0, 10)

if __name__ == "__main__":
    main()
