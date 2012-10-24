#!/usr/bin/python

#Start off by creating a default template
#Read the files to get all the information needed
#Generate an mbox of all the emails
#use bash script to send the mbox using sendmail

import sys, os, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders
from subprocess import Popen, PIPE
#We will remove these once everything is tested
import mailbox
import email.utils


def generateSalutation(utorid):
	d_line = 'Dear'
	for i in utorid:
		d_line+= " " + i

	d_line += '\n\n'
	return d_line

def generateBody(grp, asst, marks):
	b_line ='Your submission for Assignment ' + str(asst) + ' has been automarked\n\n'
	total = 0
	mark = 0
	for i in marks:
		total += int(i['total'])
		mark += int(i['mark'])

	b_line += 'You have scored ' + str(mark) + ' out of a possible '+ str(total) + ' marks.\n\n'
	b_line += 'You have scored: \n\n'

	for i in marks:
		b_line += i['name'] + ': ' + str(i['mark']) + ' out of ' + str(i['total']) + '\n'

	b_line += '\n'

	return b_line

def generateFail(grp, asst, mark):
	b_line ='Your submission for Assignment ' + str(asst) + ' has been automarked\n\n'
	b_line += 'Your submission failed. Please check attachment for the reasons\n\n'
	b_line += 'Your design score is ' + str(mark['mark']) + ' out of ' + str(mark['total']) + '\n\n'
	return b_line

def generateBye(TA):
	l_line = 'Please contact ' + TA + ' if you have further questions regarding your marks.\n\n'
	l_line += 'Best of luck for the next assignment.\n\n'
	l_line += 'ECE 344 TAs\n'
	return l_line

def parseMarkFile(grp):
	mark = []
	try:
		filename = 'os161-mark-'+ grp +'.txt'
		f = open(filename, 'r')
		for l in f.readlines():
			line = l.split(',')
			mark.append({'name': line[0], 'total': line[1], 'mark': line[2][:-1]})
		f.close()
	except IOError:
		print 'Failure Path'
	return mark

def parseDesignMark(grp):
	filename = 'designs.csv'
	f = open(filename, 'r')
	mark = {}
	for l in f.readlines():
		if grp in l:
			mark['name'] = 'Design'
			line = l.split(',')
			mark['total'] = line[1]
			mark['mark'] = line[2][:-1]
	return mark


def parseEmailFile(grp):
	#filename = '../emails.txt'
	filename = 'emails.txt'
	f = open(filename, 'r')
	utorid = []
	email = []
	for line in f.readlines():
		if grp in line:
			l = line.split(',')
			i = 0
			for value in l:
				if i == 0:
					i += 1
					continue
				elif i % 2 == 1:
					#Must be utorid
					utorid.append(value)
				else:
					#Must be email id
					email.append(value)
				i += 1
	return (utorid, email)

def generateMail(email, text, asst, grp, files):
	msg = MIMEMultipart()
	msg['From'] = "dhaval@eecg.toronto.edu"
	msg['To'] = COMMASPACE.join(email)
	#msg['Date'] = format(localtime=True)
	msg['Subject'] = 'Automarker results for Assignment ' + asst
	msg.attach(MIMEText(text))

	for f in files:
		part = MIMEBase('application', "octet-stream")
		part.set_payload( open(f,"rb").read() )
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
		msg.attach(part)

	return msg

def generateEmail(grp, asst):
	(utorid, email) = parseEmailFile(grp)
	mark = parseMarkFile(grp)
	design = parseDesignMark(grp)
	if mark is None:
		mark.append(design)
		files = ["os161-marker-" + grp + ".log"]
		body = generateFail(grp, asst)
	else:
		mark.append(design)
		files = ["os161-" + grp + ".log", "os161-marker-" + grp + ".log", "os161-tester-" + grp + ".log"]
		body = generateBody(grp, asst, mark)
	hello = generateSalutation(utorid)
	bye = generateBye("Ali Shariat <shariat@gmail.com>")
	email.append("dhaval@eecg.toronto.edu")
	email.append("shariat@gmail.com")
	message = hello + body + bye
	return generateMail(email, message, asst, grp, files)

def generateMbox(asst):
	mbox = mailbox.mbox('test.mbox')
	mbox.lock()
	try:
		for i in range(1,11):
			grp = u'%03d' % i
			email = generateEmail(grp, asst)
			print "Email for os-" + grp + " generated"
			mbox.add(email)
			mbox.flush()
			print "Email for os-" + grp + " added"
	finally:
		mbox.unlock()
	return

def sendEmail(asst):
	p = Popen(["/usr/sbin/sendmail", "-t"], stdin=PIPE)
	for i in range(1, 39):
		grp = u'%03d' % i
		email = generateEmail(grp, asst)
		print "Email for os-" + grp + " generated"
		p.communicate(email.as_string())
		print "Email for os-" + grp + " sent"


def main():
	asst = str(sys.argv[1])
	generateMbox(asst)
	#sendEmail(asst)

if __name__ == "__main__":
	main()
