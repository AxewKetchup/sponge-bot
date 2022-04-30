import pytextnow
import pyjokes
import random
import time
import requests

while True:
    try:
        spam_num = int(7783165140)
        break
    except ValueError:
        print("> Invalid: Please try again.")

print("Starting... ")

while True:
    client = pytextnow.Client("icmcplays", sid_cookie="s%3AuHz223f1zaWr9WMleFtVbMDbqzCnbo6G.76PbWClobtRtXeQ3EZSDb2C9Q2xG22EotoyCp6%2F5bpc", csrf_cookie="s%3ALVEdfHQIKfJxA8h2hBxDTzbj.eIEmb7W8s6%2Bl1qPa0xbZxcnLkkSBig8f420Aau4EqgI")
    rMsg = random.randint(1, 2)
    if (rMsg == 1):
        print("> Sending cat image.")
        
        image_url = "https://cataas.com/cat"
        img_data = requests.get(image_url).content
        with open('cat.png', 'wb') as handler:
            handler.write(img_data)

        file_path = "cat.png"
        client.send_mms(str(spam_num), file_path)

    elif (rMsg == 2):
        print("> Sending programming joke.")
        client.send_sms(str(spam_num), str(pyjokes.get_joke()))
        
    time.sleep(random.randint(2, 8))


#         client.auth_reset() 

