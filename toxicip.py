import colorama
from colorama import Fore
from pystyle import Colorate, Colors, Write, Center
import json
import requests
from termcolor import colored

print(Fore.RED + '''
    ███      ▄██████▄  ▀████    ▐████▀  ▄█   ▄████████       ▄█     ▄███████▄ 
▀█████████▄ ███    ███   ███▌   ████▀  ███  ███    ███      ███    ███    ███ 
   ▀███▀▀██ ███    ███    ███  ▐███    ███▌ ███    █▀       ███▌   ███    ███ 
    ███   ▀ ███    ███    ▀███▄███▀    ███▌ ███             ███▌   ███    ███ 
    ███     ███    ███    ████▀██▄     ███▌ ███             ███▌ ▀█████████▀  
    ███     ███    ███   ▐███  ▀███    ███  ███    █▄       ███    ███        
    ███     ███    ███  ▄███     ███▄  ███  ███    ███      ███    ███        
   ▄████▀    ▀██████▀  ████       ███▄ █▀   ████████▀       █▀    ▄████▀                                                                                    
''' + Fore.RESET)
print(Colorate.Horizontal(Colors.red_to_yellow, '''
---------------------------------------------------------------------------------
[1] $iplookup: check an ip (get infos)      |  
[2] $linkgrab: create an ip-grabber-link.   |       MADE BY BOKA_664 - Enjoy it!
---------------------------------------------------------------------------------
''', 1))

scelta = input(Fore.RED + ">$" + Fore.RESET)

if scelta == 'iplookup':
    scelta2 = input(Fore.RED + "[Insert IP]>" + Fore.RESET)
    apikey = "YOUR API KEY HERE"

    response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + apikey + '&ip_address=' + scelta2)
    result = json.loads(response.content)
    print(colored(result, 'green'))

elif scelta == 'linkgrab':
    print(Fore.GREEN + "[LINK READY ON: https://iplogger.org/logger/]" + Fore.RESET)
