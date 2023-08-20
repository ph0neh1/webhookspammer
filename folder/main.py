from discord import SyncWebhook
import time

print("Discord Webhook spammer by cr.ghost")
time.sleep(5)

webhook=input("Insert Webhook: ")
webhook = SyncWebhook.from_url(webhook)
msg=input("Insert Message: ")
sleep=int(input('Sleeping time: '))
amountofmessages=int(input('Number of messages: '))
fakecount=0

for x in range(amountofmessages):
 fakecount=fakecount+1
 webhook.send(msg)
 current_time = time.strftime("%H:%M:%S", time.localtime())
 print("<{}> Sent {}/{} messages".format(current_time, fakecount, amountofmessages))
 time.sleep(sleep)

current_time = time.strftime("%H:%M:%S", time.localtime())
print("<{}> Webhook spammer is done!".format(current_time))
input("Press any key to continue.")