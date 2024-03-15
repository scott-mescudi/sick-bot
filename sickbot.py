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
Betreft: Afwezigheid

Geachte docent,

Hierbij wil ik u laten weten dat ik vandaag niet in staat ben om naar school te komen. Want {random_excuse} Daarom zal ik vandaag niet aanwezig kunnen zijn bij de lessen.

Ik beloof om zo snel mogelijk een medische verklaring van mijn huisarts te verkrijgen en deze naar school te sturen. Mocht er nog schoolwerk zijn dat ik thuis kan doen, dan zal ik mijn best doen om dat zo spoedig mogelijk af te handelen.

Mijn oprechte excuses voor het ongemak dat dit kan veroorzaken. Ik hoop snel weer hersteld te zijn en mijn studie ononderbroken voort te kunnen zetten.

Met vriendelijke groet,
'''

letter3 = f'''
Betreft: Afwezigheid

Geachte docent,

Met spijt moet ik u informeren dat ik vandaag niet aanwezig kan zijn op school want {random_excuse}. Ik hoop dat u mijn situatie begrijpt en mijn afwezigheid kunt accepteren.

Ik zal mijn best doen om eventuele gemiste lessen in te halen en ervoor te zorgen dat ik weer op schema kom met mijn studie. Als er specifieke taken zijn die ik thuis kan voltooien, laat het me dan alstublieft weten.

Mijn excuses voor het eventuele ongemak dat dit kan veroorzaken. Ik hoop snel weer terug te zijn op school en mijn studie voort te zetten.

Met vriendelijke groet,
'''

letter4 = f'''
Betreft: Afwezigheid 

Geachte docent,

Helaas kan ik vandaag niet aanwezig zijn op school want {random_excuse}. Hierdoor ben ik niet in staat om naar school te komen. Ik bied mijn excuses aan voor eventuele ongemakken die hierdoor kunnen ontstaan.

Ik zal proberen om zoveel mogelijk van het gemiste werk in te halen en ervoor te zorgen dat ik weer op schema kom met mijn studie. Als er specifieke taken zijn die ik thuis kan doen, laat het me dan alstublieft weten.

Nogmaals mijn excuses voor het ongemak. Ik hoop snel de nodige oplossingen te vinden en mijn studie ononderbroken voort te zetten.

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
body = random.choice([letter, letter3, letter4])
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
