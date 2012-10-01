#!/usr/bin/python

import core
import sys

def catmouse(test, cmd):
        result = 0
	test.send_command(cmd)

        bowls = [ -1, -1]
        mouse_cat = 0

        # look for 64 outputs = 
        # 8 (6 cats + 2 mouse) * 2 (start, end) * 4 iterations
        for i in range(64):
            out = test.look_for( \
                ['cat: (\d) starts eating: bowl (\d), iteration (\d)', \
                     'cat: (\d) ends eating: bowl (\d), iteration (\d)', \
                     'mouse: (\d) starts eating: bowl (\d), iteration (\d)', \
                     'mouse: (\d) ends eating: bowl (\d), iteration (\d)'])
            if out < 0:
                result = -1 # no match failure
                break
            # go to show output
            print str(i) + ': ' + test.kernel().match.group(0)

            nr, bowl, iteration = test.kernel().match.groups()
            nr = int(nr)
            bowl = int(bowl)
            iteration = int(iteration)

            # sanity check
            if bowl < 1 or bowl > 2:
                print 'bowl nr should be 1 or 2'
                print bowl
                result = -1
                break

            if iteration < 0 or iteration > 3:
                print 'iteration should be 0, 1, 2 or 3'
                result = -1
                break
            
            if out == 0 or out == 1:
                if nr < 0 or nr > 6:
                    print 'cat nr should be 1-6'
                    result = -1
                    break
            else:
                if nr < 0 or nr > 1:
                    print 'mouse nr should be 1-6'
                    result = -1
                    break

            # now check that the cat/mouse consistency is met
            bowl = bowl - 1
            if out == 0:
                if mouse_cat == 2:
                    print 'mouse is already eating'
                    result = -1
                    break
                mouse_cat = 1
                if bowls[bowl] != -1:
                    print 'bowl = ' + str(bowl) + 'is already in use'
                    result = -1
                    break
                bowls[bowl] = nr

            elif out == 1:
                if bowls[bowl] != nr:
                    print 'cat = ' + str(nr) + 'exiting without entering'
                    result = -1
                    break
                bowls[bowl] = -1
                empty = 1
                for i in range(2):
                    if bowls[i] != -1:
                        empty = 0
                if empty == 1:
                    mouse_cat = 0

            elif out == 2:
                if mouse_cat == 1:
                    print 'cat is already eating'
                    result = -1
                    break
                mouse_cat = 2
                if bowls[bowl] != -1:
                    print 'bowl = ' + str(bowl) + 'is already in use'
                    result = -1
                    break
                bowls[bowl] = nr

            elif out == 3:
                if bowls[bowl] != nr:
                    print 'mouse = ' + str(nr) + 'exiting without entering'
                    result = -1
                    break
                bowls[bowl] = -1
                empty = 1
                for i in range(2):
                    if bowls[i] != -1:
                        empty = 0
                if empty == 1:
                    mouse_cat = 0

        return result

def main():
	global test
        result = 0

        # try cat with semaphores
	kernel_name = str(sys.argv[1])
	test = core.TestUnit(kernel_name, "Testing cat/mouse using semaphores")
        result = catmouse(test, '1a')
        if result < 0:
            # try cat with locks
            test = core.TestUnit(kernel_name, "Testing cat/mouse using locks")
            result = catmouse(test, '1b')
        test.print_result(result)

if __name__ == "__main__":
	main()

