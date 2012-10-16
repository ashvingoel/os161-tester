#!/usr/bin/python

import pexpect
import sys
import os

class TestUnit:
	#Implicit assumptions, sys161 is in path

	def set_log_file(self):
		self.kernel.logfile = open('os161-marker.txt', 'a')

	def __init__(self, path_to_kernel, message, grade=False):
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
		self.total_mark = 0
                print message
		if grade == True:
			self.set_log_file()

	def clean_kernel(self):
		self.kernel.logfile.close()
		print 'Mark for test is ' + str(self.total_mark)

        # def kernel(self):
        #         return self.kernel

        # def verbose(self):
        #         return self.verbose

	#We need to wait before we can actually send a command.
	def send_command(self, cmd):
		self.kernel.expect('OS\/161 kernel \[\? for menu\]\: ')
		#The fun bit is, we need to send the command character by
		#character to the simulator, otherwise we are going to have
		#a lot of fun ;-)
                if self.verbose > 1:
                        print "SENDING: " + cmd
		cmd_char = list(cmd)
		for i in cmd_char:
			self.kernel.send(i)
		self.kernel.send('\n')
		return

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
			return -1
                except Exception:
                        print "UNEXPECTED ERROR", sys.exc_info()[0]
			return -1
		return index

        def print_result(self, out):
                if out >= 0:
                        print "PASS"
                else:
                        print "FAIL"

	def look_for_and_print_result(self, result, mark=0):
                out = self.look_for(result)
                self.print_result(out)
		self.total_mark += mark

	def look_for_and_return_mark(self, result, mark):
		out = self.look_for(result)
		if out >= 0:
			return mark
		return 0

