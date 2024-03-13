import smtplib
import random 
import datetime
import time
import sys
import pygame
from colorama import Fore, init
import math
import json

init(autoreset=True)

def read_config(filename='config.json'):
    with open(filename) as f:
        config = json.load(f)
    return config

config = read_config()


def sender():
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_email, to_email, message)

def play_audio_file(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except pygame.error:
        print("Error: Unable to load or play the audio file.")

random_excuse = random.choice([
    "ik heb last van hoge koorts.",
    "ik heb last van overgeven en diarree.",
    "ik heb een afspraak bij de dokter.",
    "ik heb last van een blessure."
])

letter = f'''
Betreft: Ziektemelding

Geachte docent,

Hierbij wil ik u laten weten dat ik vandaag niet in staat ben om naar school te komen. Want {random_excuse} Daarom zal ik vandaag niet aanwezig kunnen zijn bij de lessen.

Ik beloof om zo snel mogelijk een medische verklaring van mijn huisarts te verkrijgen en deze naar school te sturen. Mocht er nog schoolwerk zijn dat ik thuis kan doen, dan zal ik mijn best doen om dat zo spoedig mogelijk af te handelen.

Mijn oprechte excuses voor het ongemak dat dit kan veroorzaken. Ik hoop snel weer hersteld te zijn en mijn studie ononderbroken voort te kunnen zetten.

Met vriendelijke groet,
'''

target_hour = int(input("\nEnter the hour: "))                                 
target_minute = int(input("Enter the minute: "))
print("alarm will go off at ", target_hour,":",target_minute)

smtp_server = config['smtp_server']
smtp_port = config['smtp_port']
smtp_username = config['smtp_username']
smtp_password = config['smtp_password']
from_email = config['from_email']
to_email = config['to_email']
audio_file_path = config['audio_file_path']

a = random.randint(120, 7200)

subject = 'Afwezigheid'
body = letter
message = f'Subject: {subject}\n\n{body}'

print("Goodnight...")
while True:
    local_time = datetime.datetime.now()
    if local_time.hour == target_hour and local_time.minute == target_minute:
        print(Fore.RED + "\nWake up!!!")
        play_audio_file(audio_file_path) # Uncomment this line when you want to play the audio file.0
        print(Fore.YELLOW + f"You have {math.ceil(a / 60)} minutes to close the program or the email will send (press ctrl + c to close)")
        time.sleep(a)
        sender()
        sys.exit()
