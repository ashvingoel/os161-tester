#!/usr/bin/python

import pexpect
import sys
import os
import shutil

class TestUnit:
        # we assume that sys161 is in path
        def set_timeout(self, timeout):
            self.kernel.timeout = timeout
            if self.verbose > 0:
                print 'This test has a timeout of ' + str(timeout) + ' seconds'

        def __init__(self, message, path_to_kernel = "kernel"):
                try:
                        self.verbose = os.environ['OS161_TESTER_VERBOSE']
                except KeyError:
                        self.verbose = 0
                try:
                        self.verbose = int(self.verbose)
                except ValueError:
                        self.verbose = 0

                try:
                        self.swapping = os.environ['OS161_SWAPPING']
                except KeyError:
                        self.swapping = 0
                try:
                        self.swapping = int(self.swapping)
                except ValueError:
                        self.swapping = 0

                path = 'sys161 ' + str(path_to_kernel)
                self.kernel = pexpect.spawn(path, timeout = 10)
                self.mark = 0
                self.total = 0
                self.crashed = 0
                self.message = message
                print message
                # pexpect copies all input and output to this file
                self.kernel.logfile = open('os161-pexpect.log', 'a')
                self.cwd = os.getcwd()
                self.prog = "/testbin/os161testerprog"
                self.errors = {'CRASHED' : -1, 'TIMEOUT' : -2, 'EOF' : -3,
                               'BUG' : -4 }

        def __del__(self):
                self.kernel.logfile.close()
                if self.total > 0:
                        print 'Mark for ' + self.message + ' is ' + \
                                str(self.mark) + ' out of ' + str(self.total)
                        marker = open('os161-mark.txt', 'a')
                        marker.write(self.message + ', ' + str(self.mark) + \
                                     ', ' + str(self.total) + '\n')
                        marker.close()
                try:
                        os.remove(self.cwd + self.prog)
                except OSError:
                        pass

        # def kernel(self):
        #         return self.kernel

        # def verbose(self):
        #         return self.verbose

        # wait for menu
        def wait_for_menu(self, wait):
                if wait == 0:
                    return
                try:
                        self.kernel.expect('OS\/161 kernel \[\? for menu\]\: ')
                except Exception:
                        self.crashed = 1
                        print 'OS HAS CRASHED'

        # By default, we wait before we send a command.
        # However, if wait is set to 0, then we don't wait AND
        # we don't send the newline.
        def send_command(self, cmd, wait = 1):
                self.wait_for_menu(wait)
                if self.crashed > 0:
                        return
                if self.verbose > 1:
                        print "SENDING: " + cmd
                # The fun bit is, we need to send the command character by
                # character to the simulator, otherwise we are going to have
                # a lot of fun ;-)
                cmd_char = list(cmd)
                for i in cmd_char:
                        self.kernel.send(i)
                if wait:
                    self.kernel.send('\n')

        def send_command_no_wait(self, cmd):
                self.send_command(cmd, 0)

        def runprogram(self, cmd, args = ""):
                # self.send_command("p " + cmd + " " + args);
                # make a copy of the program, so that students don't try 
                # to guess the output of a program by its name
                if self.verbose > 1:
                        print "Running: " + "p " + cmd + " " + args
                shutil.copy(self.cwd + cmd, self.cwd + self.prog)
                self.send_command("p " + self.prog + " " + args);

        def look_for(self, result):
                if (self.crashed > 0):
                        return self.errors['CRASHED']
                try:
                        if self.verbose > 1:
                                print "EXPECTING: " + str(result)
                        index = self.kernel.expect(result)
                        # print "BEFORE: \"" + self.kernel.before + "\""
                        if self.verbose > 0:
                                print "FOUND: " + self.kernel.match.group(0)
                except pexpect.TIMEOUT, e:
                        print "TIMEOUT ERROR"
                        return self.errors['TIMEOUT']
                except pexpect.EOF:
                        print "END OF FILE ERROR"
                        return self.errors['EOF']
                except Exception, e:
                        print "UNEXPECTED ERROR", sys.exc_info()[0]
                        print "\nPLEASE REPORT THIS TO THE INSTRUCTOR OR A TA\n"
                        return self.errors['BUG']
                return index

        def print_result(self, mark_obtained, mark, wait = 1):
                self.total += mark
                self.mark += mark_obtained
                if mark_obtained > 0:
                    self.wait_for_menu(wait)
                if (mark_obtained == mark) and (self.crashed == 0):
                        print "PASS"
                else:
                        print "FAIL"


        def look_for_and_print_result(self, result, mark, wait = 1):
                out = self.look_for(result)
                if out >= 0:
                        self.print_result(mark, mark, wait)
                else:
                        self.print_result(0, mark)

        def look_for_and_print_result_no_wait(self, result, mark):
                self.look_for_and_print_result(result, mark, 0)
