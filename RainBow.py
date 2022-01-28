import ctypes
import requests
import random
import string
import time
import os
import sys
import colorama
from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.MAGENTA + '╦═╗╔═╗╦╔╗╔╔╗ ╔═╗╦ ╦╔═╗╔═╗╔╗╔')
print(Fore.BLUE + '╠╦╝╠═╣║║║║╠╩╗║ ║║║║║ ╦║╣ ║║║')
print(Fore.CYAN + '╩╚═╩ ╩╩╝╚╝╚═╝╚═╝╚╩╝╚═╝╚═╝╝╚╝')
print(Fore.BLUE + '╔══════════════════════════════════════════════╗')
print(Fore.CYAN + '║ Dev:T0XICDEV#2686 Name: rainbowdog#6114      ║')
print(Fore.BLUE + '║ Host This gen at batcore.eu/affiliate/Toxic  ║')
print(Fore.CYAN + '║ !! THIS IS NOT OFFICIAL BATCORE GEN XD !!    ║')
print(Fore.BLUE + '╚══════════════════════════════════════════════╝')
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(10):
    time.sleep(0.4)
    sys.stdout.write("\rLoading RainBowGEN   " + animation[i % len(animation)])
    sys.stdout.flush()
print('')
print(Back.MAGENTA + Fore.BLUE + 'Welcome To RainbowGEN')
print(Style.RESET_ALL)
time.sleep(1.0)

print(Back.CYAN + Fore.WHITE + '')
num = int(input('Amount of codes ?'))

with open("rainbow.txt", "w", encoding='utf-8') as file:
    print("Reading txt ...")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(Back.MAGENTA + Fore.BLUE + '>>>| RAINBOW GEN |<<<')
    time.sleep(1.0)
    print(Back.BLUE + Fore.MAGENTA + '')
    print(f"Starting generating {num} codes!")
    print(Style.RESET_ALL)
with open("rainbow.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" WORKS | {nitro} ")
            break
        else:
            print(Fore.RED + f"It work?,ne! | {nitro} ")


print(Back.RED + Fore.WHITE +"Join BATCORE FOR HAVING BETTER LIFE ! : https://discord.gg/batcore And use  https://batcore.eu/affiliate/Toxic\n")

time.sleep(0.6)

input("I like spending your time of thinking you get nitro HAHA")
