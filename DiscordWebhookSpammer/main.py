import os
import time

os.system('cls||clear')
print("Downloading and installing required files... (This can take awhile)")
os.system("title Discord Webhook Spammer V1.2")
os.system("pip3 install Discord")
os.system("pip3 install requests")

from discord import SyncWebhook

class TextColor:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"

os.system('cls||clear')
print("Discord Webhook Spammer version 1.2 by cr.ghost")
print("https://github.com/ph0neh1/webhookspammer")
print(".")
time.sleep(5)
webhook=input(TextColor.GREEN + "<Settings>" + TextColor.RESET + " " + "Insert Webhook: ")
webhook = SyncWebhook.from_url(webhook)
msg=input(TextColor.GREEN + "<Settings>" + TextColor.RESET + " " + "Insert Message: ")
sleep=int(input(TextColor.GREEN + "<Settings>" + TextColor.RESET + " " + "Insert sleeping time: "))
amountofmessages=int(input(TextColor.GREEN + "<Settings>" + TextColor.RESET + " " + "Insert amount of messages: "))
fakecount=0

for x in range(amountofmessages):
 fakecount=fakecount+1
 webhook.send(msg)
 current_time = time.strftime("%H:%M:%S", time.localtime())
 print(TextColor.RED + "<Main>" + TextColor.RESET + " " + "[{}] Sent {}/{} messages".format(current_time, fakecount, amountofmessages))
 time.sleep(sleep)

current_time = time.strftime("%H:%M:%S", time.localtime())
print("<{}> Webhook spammer is done!".format(current_time))
input("Press any key to continue.")