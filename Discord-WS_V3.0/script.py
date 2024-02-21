import os

# Installing required modules
os.system('pip3 install discord')
os.system('pip3 install requests')
os.system('pip3 install customtkinter')

from tkinter import *
from discord import SyncWebhook
import customtkinter
import time

class TextColor:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"

art = '''
⠀⠀⠀⠀⠀⢸⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠀⠀⠑⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠙⢤⡷⣤⣦⣀⠤⠖⠚⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⡿⠢⢄⡀⠀⡇⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠸⠷⣶⠂⠀⠀⠀⣀⣀⠀⠀⠀
⢸⣃⠀⠀⠉⠳⣷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⢉⡭⠋
⠀⠘⣆⠀⠀⠀⠁⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀
⠀⠀⠘⣦⠆⠀⠀⢀⡎⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⡀⣠⠔⠋⠀⠀⠀⠀
⠀⠀⠀⡏⠀⠀⣆⠘⣄⠸⢧⠀⠀⠀⠀⢀⣠⠖⢻⠀⠀⠀⣿⢥⣄⣀⣀⣀⠀⠀
⠀⠀⢸⠁⠀⠀⡏⢣⣌⠙⠚⠀⠀⠠⣖⡛⠀⣠⠏⠀⠀⠀⠇⠀⠀⠀⠀⢙⣣⠄
⠀⠀⢸⡀⠀⠀⠳⡞⠈⢻⠶⠤⣄⣀⣈⣉⣉⣡⡔⠀⠀⢀⠀⠀⣀⡤⠖⠚⠀⠀
⠀⠀⡼⣇⠀⠀⠀⠙⠦⣞⡀⠀⢀⡏⠀⢸⣣⠞⠀⠀⠀⡼⠚⠋⠁⠀⠀⠀⠀⠀
⠀⢰⡇⠙⠀⠀⠀⠀⠀⠀⠉⠙⠚⠒⠚⠉⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢧⡀⠀⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣶⣶⣿⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠀⠀⠀⠙⢿⣳⠞⠳⡄⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠹⣄⣀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

# Initialize global variables
Textt = ""
Sleepp = 0
Amountt = 0
fakecount = 0

def resetcount():
    global fakecount
    fakecount=0

def button1_event():
    global webhookk
    webhook = customtkinter.CTkInputDialog(text="Enter Discord Webhook here:", title="Webhook")
    webhookk = SyncWebhook.from_url(webhook.get_input())

def button2_event():
    global Textt
    Text = customtkinter.CTkInputDialog(text="Change Text:", title="Text Message")
    Textt = Text.get_input()

def button3_event():
    global Sleepp
    Text = customtkinter.CTkInputDialog(text="Change Sleep Time:", title="Sleep Time")
    Sleepp = int(Text.get_input())

def button4_event():
    global Amountt
    Text = customtkinter.CTkInputDialog(text="Change Amount of Messages:", title="Amount of Messages")
    Amountt = int(Text.get_input())

def button5_event():
    global fakecount
    for x in range(Amountt):
        fakecount += 1
        webhookk.send(Textt)
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(TextColor.RED + "<Main>" + TextColor.RESET + " " + "[{}] Sent {}/{} messages".format(current_time, fakecount, Amountt))
        time.sleep(Sleepp)
        if fakecount == Amountt:
            resetcount()

# Creating GUI
root = customtkinter.CTk()
root.title("Discord-WS V3.0")
root.geometry("300x200")
root.resizable(False,False)

button1 = customtkinter.CTkButton(master=root, text="Change Discord Webhook", command=button1_event)
button1.place(relx=0.5, rely=0.1, anchor=CENTER)
button2 = customtkinter.CTkButton(master=root, text="Change Text", command=button2_event)
button2.place(relx=0.5, rely=0.3, anchor=CENTER)
button3 = customtkinter.CTkButton(master=root, text="Change Sleep Time", command=button3_event)
button3.place(relx=0.5, rely=0.5, anchor=CENTER)
button4 = customtkinter.CTkButton(master=root, text="Change Amount of Messages", command=button4_event)
button4.place(relx=0.5, rely=0.7, anchor=CENTER)
button5 = customtkinter.CTkButton(master=root, text="Execute Script", command=button5_event)
button5.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()