#!/usr/bin/python

import pexpect
import sys
import os
import shutil

class TestUnit:
	#Implicit assumptions, sys161 is in path
	def set_log_file(self):
		self.kernel.logfile = open('os161.log', 'a')

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
		path = 'sys161 ' + str(path_to_kernel)
		self.kernel = pexpect.spawn(path, timeout = 10)
		self.mark = 0
		self.total = 0
		self.message = message
                print message
		self.set_log_file()
                self.cwd = os.getcwd()
                self.prog = "/testbin/os161testerprog"

	def __del__(self):
		self.kernel.logfile.close()
                if (self.total > 0):
                    print 'Mark for ' + self.message + ' is ' + \
                        str(self.mark) + ' out of ' + str(self.total)
                    marker = open('os161-mark.txt', 'a')
                    marker.write(self.message + ', ' + str(self.total) + \
                                     ', ' + str(self.mark) + '\n')
                    marker.close()
                try:
                    os.remove(self.cwd + self.prog)
                except OSError:
                    pass

        # def kernel(self):
        #         return self.kernel

        # def verbose(self):
        #         return self.verbose

	# By default, we wait before we send a command.
        # However, if wait is set to 0, then we don't wait AND
        # we don't send the newline.
	def send_command(self, cmd, wait = 1):
                if wait:
                    try:
			self.kernel.expect('OS\/161 kernel \[\? for menu\]\: ')
                    except Exception:
			print 'OS HAS CRASHED'
		#The fun bit is, we need to send the command character by
		#character to the simulator, otherwise we are going to have
		#a lot of fun ;-)
                if self.verbose > 1:
                        print "SENDING: " + cmd
		cmd_char = list(cmd)
		for i in cmd_char:
			self.kernel.send(i)
                if wait:
                    self.kernel.send('\n')

        def runprogram(self, cmd, args = ""):
            # make a copy of the program, so that students don't try 
            # to guess the output of a program by its name
            shutil.copy(self.cwd + cmd, self.cwd + self.prog)
            self.send_command("p " + self.prog + " " + args);

	def look_for(self, result):
		try:
                        if self.verbose > 1:
                                print "EXPECTING: " + str(result)
			index = self.kernel.expect(result)
                        if self.verbose > 0:
                                print "FOUND: " + self.kernel.match.group(0)
                except pexpect.TIMEOUT, e:
                        print "TIMEOUT ERROR"
			return -1
                except pexpect.EOF:
                        print "END OF FILE ERROR"
			return -2
                except Exception, e:
                        print "UNEXPECTED ERROR", sys.exc_info()[0]
			print "\nPLEASE REPORT THIS TO THE INSTRUCTOR OR A TA\n"
			return -3
		return index

        def print_result(self, mark_obtained, mark):
		self.total += mark
		self.mark += mark_obtained
                if mark_obtained == mark:
                        print "PASS"
                else:
                        print "FAIL"


	def look_for_and_print_result(self, result, mark):
                out = self.look_for(result)
		if (out >= 0):
			self.print_result(mark, mark)
		else:
			self.print_result(0, mark)
