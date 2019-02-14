import smtplib
import pendulum as pen
import jsonlines
import argparse

from sys import exit

from pandas import read_excel

from smtplib import SMTPAuthenticationError
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from code_generator import code_generator


parser = argparse.ArgumentParser(description='Bulk Email Sender')
parser.add_argument('--senders', type=str, help='The Excel file for sending. Example: --senders="senders.xlsx"')
parser.add_argument('--receivers', type=str, help='The Excel file for receivers. Example: --receivers="receivers.xlsx"')
args = parser.parse_args()

senders = read_excel(args.senders, encoding='utf-8')
sender_emails = senders['Emails']
sender_passwords = senders['Passwords']
sender_smtp_servers = senders['SMTP']
sender_smtp_ports = senders['Ports']
receivers = read_excel(args.receivers, encoding='utf-8')
receiver_emails = receivers['Emails']

receiver_count = 0

the_date = pen.now().format('dddd_DD_YYYY')


def send_mail(username, password, server, port, receiver):
	
	global the_time
	
	the_time = pen.now().format('h:mm A')
	
	global CG
	
	CG = code_generator()
	
	server = smtplib.SMTP(server, port)
	server.starttls()
	server.login(username, password)
	CG = code_generator()
	message = MIMEMultipart("alternative")
	message["Subject"] = "Whatever your subject may be..."
	message["From"] = username
	message["To"] = receiver
	msg = """\
	<html>
	  <body>
		<p>Hi,<br>
		   How are you?<br>
		   <a href="http://www.realpython.com">Real Python</a> 
		   has many great tutorials.
		</p>
	  </body>
	</html>
	"""
	part1 = MIMEText(msg, "html")
	message.attach(part1)
	server.sendmail(username, receiver, message.as_string())
	server.quit()
	
def max_senders():
	
	global the_date 
	global receiver_count
	
	with jsonlines.open(the_date+'.json','a') as writer:
		for x in range(0, len(sender_emails) ):
			try:
				u = sender_emails[x]
				p = sender_passwords[x]
				s = sender_smtp_servers[x]
				pp = str(sender_smtp_ports[x])
				r = receiver_emails[receiver_count]
			except KeyError:
				exit(0)

			# if for some reason the sending doesnt work, skip the sender
			#                      ,and let another, send to the receiver
			try:
				send_mail(username=u, password=p, server=s, port=pp, receiver=r)
				
				#print("from:" + u)
				#print("    to:" + r)
				print('from: '+'example@*.com')
				print('to: '+'example@*.com')
				
				my_dict = dict()
				my_dict['receiver'] = r
				my_dict['identifier'] = CG
				my_dict['sender'] = u
				my_dict['date'] = the_date
				my_dict['time'] = the_time
				
				writer.write(my_dict)
			
				receiver_count += 1
				
				
			except SMTPAuthenticationError:
				pass

def mass():

	global receiver_count

	while receiver_count <= len(receiver_emails):
		
		max_senders()
		

if __name__ == "__main__":		
	mass()
