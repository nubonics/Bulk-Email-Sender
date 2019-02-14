
# Description
This program is designed to send one email at a time to a recipient. Each email takes approximately one second to send after the script is started.
The ratio this program works on is a one to one, meaning for each sender in the senders excel list/file it will send one email to the recipient. The next sender in the senders excel list/file will send an email to the next recipient in the recipients excel list/file. If there are less senders than recipients the program will accommodate by using senders multiple times. If there are 100 senders and 1000 recipients. Each sender will send 10 emails, and each recipient will only receive one email. From the recipients perspective, they have a 10% chance of receiving an email from a specific sender compared to another recipient, given the number of senders and recipients in the example above.
Worthy note: If there are 100 senders, the first sender will only send one email, until all the other senders have sent their email to their recipient, only then, will the first sender send an email again to another recipient. This means, if there are 97 recipients, and 100 senders, only 97 senders will actually send an email.
Second worthy note: This program is designed to send the same html to ALL recipients.
### Testing
 Script was tested on port 587 and runs flawlessly as of Feburary 2nd 2019

### Data
Information is stored via a JSON file with the format of: Saturday_2_2_2019.json in the current working directory.

### Requirements:

     pip install -r requirements.txt

 - All senders must have smtp enabled
 - For the best results to get the email(s) directly into the recipients
   inbox, the recipient must have had to read an email from the sender
   before.
 - senders.xslx must have the columns
   - Emails
   - Passwords
   - SMTP
   - Ports
 - receivers.xlsx must have the column
    -  Emails

### USAGE:
	python simple_bulk_email_sender.py --senders="senders.xlsx" --receivers="receivers.xlsx"
