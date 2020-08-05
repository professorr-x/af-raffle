import requests
import names
from colorama import init
from colorama import Fore, Back, Style
from datetime import datetime
import time as t
from random import randrange

init(autoreset=True)
### Find the post URL and payload each time

POST_URL = 'https://docs.google.com/forms/d/1zegX7ajXCukRTEIrbKapT8F3HekR0oQGpESSRF36_Xs/formResponse'


headers = {
    'Accept': 'application/xml, text/xml, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Client-Data': 'CI+2yQEIprbJAQiqncoBCIOhygEIx6vKAQjbrMoBCJ2wygEIi7TKAQj4tMoBCJm1ygEI0bXKAQjutcoBCIG2ygEIvbbKAQjot8oBCP+8ygEImb3KAQi9vcoBCPfHygEI58jKAQjqyMoBCOvIygEI8sjKAQiqycoBCO3JygEIssvKAQ==',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty'
}

counter = 0

while True:
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Generating Random Name'.format(str(dateTimeObj)))
    payload = 'entry.1089277187=WMNS%20Air%20Jordan%204%20Retro%20SP%20%28Sail/%20Muslin-White-Black%29&entry.1952962866={}&entry.2011436433=US%206.5%20/%20UK%204%20/%20EU%2037.5&entry.638818998={}&entry.742914399=CV9388%20100-US%206.5%20/%20UK%204%20/%20EU%2037.5&entry.848461347=07931904379&entry.916445513={}@xxxxx.co.uk'.format(lastname, firstname, firstname)
    client=requests.Session()
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Starting new session'.format(str(dateTimeObj)))
    client.get('https://www.amongstfew.com/drops', headers=headers)
    r=client.post(POST_URL, headers=headers, data=payload)
    counter += 1
    dateTimeObj = datetime.now()
    print(Fore.YELLOW + '[{}] Entering {} into raffle'.format(str(dateTimeObj), firstname))
    dateTimeObj = datetime.now()
    print(Fore.GREEN + '[{}] #{} Raffle Entry Successful'.format(str(dateTimeObj),counter))
    wait = randrange(20)
    print(Fore.CYAN + '[{}] waiting {} seconds'.format(str(dateTimeObj), wait))
    t.sleep(wait)


