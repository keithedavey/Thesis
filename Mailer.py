#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mailer.py: Provides mailing functionality"""

__appname__ = "Main.py"
__author__ = "Keith E. Davey"
__email__ = "keithedavey@gmail.com"
__version__ = "0.1"
__license__ = "GNU GPL 3.0"

###########
# Modules #
###########
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

# mail() function #
# Sends mail specifying to information, and from email as 'username@domain.com', pwd in plaintext, server as smtp.domain.com, port as XXX #
# Example: mail('joe@gmail.com', 'Hello!', 'Just saying hi!', '', 'test@gmail.com', 'testpass', 'smtp.gmail.com', 587)
def mail(to_email, subject, text, attach, from_email, pwd, server, port):
	msg = MIMEMultipart()

	msg['From'] = from_email
	msg['To'] = to
	msg['Subject'] = subject

	msg.attach(MIMEText(text))

	if attach != None:
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(open(attach, 'rb').read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachement; filename="%s"' % os.path.basename(attach))
		msg.attach(part)

	mailServer = smtplib.SMTP(server, port)
	mailServer.ehlo()
	mailServer.starttls()
	mailServer.ehlo()
	mailServer.login(from_email, pwd)
	mailServer.sendmail(from_email, to_email, msg.as_string())
	mailServer.close()
