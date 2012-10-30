#!/Usr/bin/python

import pexpect
import sys
import os

class TestUnit:
	#Implicit assumptions, sys161 is in path

	def set_log_file(self):
		self.kernel.logfile = open('os161.log', 'a')

	def __init__(self, path_to_kernel, message):
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

	def __del__(self):
		self.kernel.logfile.close()
                if (self.total > 0):
                    print 'Mark for test is ' + str(self.mark) + ' out of ' + \
                        str(self.total)
                    marker = open('os161-mark.txt', 'a')
                    marker.write(self.message + ', ' + str(self.total) + \
                                     ', ' + str(self.mark) + '\n')
                    marker.close()

        # def kernel(self):
        #         return self.kernel

        # def verbose(self):
        #         return self.verbose

	#We need to wait before we can actually send a command.
	def send_command(self, cmd):
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
		self.kernel.send('\n')

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
