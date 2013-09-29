#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
from User import User
from Post import Post
from PostList import PostList

gmail_user = "dealflagger@gmail.com"
gmail_pwd = "uofthacks2013"

def mail(to, subject, text):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   #part = MIMEBase('application', 'octet-stream')
   #part.set_payload(open(attach, 'rb').read())
   #Encoders.encode_base64(part)
   #part.add_header('Content-Disposition')
   #msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

def mailAll(users):
   for x in range (len(users)):
      H = users[x].post_list.l
      for y in range (len(H)):
         mail(users[x].key, "You deal has arrived!", H[y].title)

