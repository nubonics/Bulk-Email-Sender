NOTE:
	Script was tested on port 587 and runs flawlessly as of Feburary 2nd 2019

NOTE:
	Information is stored via a JSON file with the format of: Saturday_2_2_2019.json in the current working directory.

Requirements:
	senders.xslx must have the columns    Emails	  Passwords	  SMTP	  Ports
	receivers.xlsx must have the column   Emails
	pip install -r requirements.txt

USAGE:
	python simple_bulk_email_sender.py --senders="senders.xlsx" --receivers="receivers.xlsx"