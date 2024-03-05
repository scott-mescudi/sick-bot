import smtplib
import random 
import datetime
import time
import sys

###########################################################
target_hour = int(input("Enter the hour: "))                                 
target_minute = int(input("Enter the minute: "))
print("alarm will go off at ", target_hour,":",target_minute)                                     
########################################################

def sender():
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)

random_excuse = random.choice([
    "ik heb last van hoge koorts.",
    "ik heb last van overgeven en diarree.",
    "ik heb een afspraak bij de dokter.",
    "ik heb last van een blessure."
])

letter = '''
Betreft: Ziektemelding

Geachte docent,

Hierbij wil ik u laten weten dat ik vandaag niet in staat ben om naar school te komen. Want ''' + random_excuse +''' Daarom zal ik vandaag niet aanwezig kunnen zijn bij de lessen.

Ik beloof om zo snel mogelijk een medische verklaring van mijn huisarts te verkrijgen en deze naar school te sturen. Mocht er nog schoolwerk zijn dat ik thuis kan doen, dan zal ik mijn best doen om dat zo spoedig mogelijk af te handelen.

Mijn oprechte excuses voor het ongemak dat dit kan veroorzaken. Ik hoop snel weer hersteld te zijn en mijn studie ononderbroken voort te kunnen zetten.

Met vriendelijke groet,

'''

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'  # Replace with your email
smtp_password = 'your_password'          # Replace with your password

from_email = 'your_email@gmail.com'      # Replace with your email
to_email = 'recipient_email@gmail.com'    # Replace with recipient's email
subject = 'Afwezigheid'
body = letter

message = f'Subject: {subject}\n\n{body}'
print ("Goodnight...")
while True:
    local_time = datetime.datetime.now()
    if local_time.hour == target_hour and local_time.minute == target_minute:
        print("You have 20 minutes to close the program or the email will send")
        time.sleep(1200)
        sender()
        sys.exit()

