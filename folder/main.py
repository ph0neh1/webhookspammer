from discord import SyncWebhook
import time
print("created by cr.ghost")
time.sleep(5)

webhook=input("Insert Webhook: ")
msg=input("Insert Message: ")
sleep=int(input('Sleeping time: '))
num=int(input('Number of messages: '))
fakenum=0

webhook = SyncWebhook.from_url(webhook)
for x in range(num):
 fakenum=fakenum+1
 webhook.send(msg)
 print("Sent", fakenum, "/", num, "of messages")
 time.sleep(sleep)