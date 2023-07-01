import requests
import time
import pystyle
from pystyle import Colors, Colorate

def send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url=None):
    payload = {
        'username': username,
        'content': message,
        'avatar_url': avatar_url
    }
    print(Colorate.Horizontal(Colors.black_to_white,"""
    Spamming..."""))

    for _ in range(num_messages):
        requests.post(webhook_url, json=payload)
        time.sleep(cooldown)

    print(Colorate.Horizontal(Colors.black_to_white,"""
    Spam ok."""))

def delete_webhook(webhook_url):
    requests.delete(webhook_url)

print(Colorate.Horizontal(Colors.red_to_white, """
             {/\}=_____________________________={/\}                                      
            /\|||||Create By NightfoxDEV|||||\/
                  {/\Made by french hacker/\}                                                                                                       
"""))

webhook_url = input(Colorate.Horizontal(Colors.red_to_purple, """

Entrez l'url du webhook : """))
username = input(Colorate.Horizontal(Colors.red_to_purple, "Quel est le nom du webhook : "))
message = input(Colorate.Horizontal(Colors.red_to_purple, "Message : "))
num_messages = int(input(Colorate.Horizontal(Colors.red_to_black, "Combien de message voulez vous envoyez : ")))
cooldown = int(input(Colorate.Horizontal(Colors.red_to_white, "temps entre chaque message (0 = no cooldown): ")))
avatar_url = input(Colorate.Horizontal(Colors.red_to_purple, "Lien de l'avatar : "))

send_webhook_message(webhook_url, username, message, num_messages, cooldown, avatar_url)

delete_webhook_input = input(Colorate.Horizontal(Colors.red_to_purple, """
Do you want to delete the webhook ? (y/n) : """))
if delete_webhook_input.lower() == "y":
    delete_webhook(webhook_url)
    print(Colorate.Horizontal(Colors.Black_to_purple,"    Webhook supprimer."))


