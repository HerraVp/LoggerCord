import discord
from discord.ext import commands
from config.config import *
import os
import sys
import datetime
import requests
import asyncio
from colorama import Fore

client = discord.Client()

if os.name == "nt":
    os.system("cls")
    os.system("title LoggerCord")
if os.name == "posix":
    os.system("clear")


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


def install(package):
    os.system(f"{sys.executable} -m pip install {package}")


def uninstall(package):
    os.system(f"{sys.executable} -m pip uninstall {package}")


if "discord.py" in sys.modules:
    uninstall("discord.py")

if "discordselfbot" in sys.modules:
    uninstall("discordselfbot")

try:
    import discord
except ModuleNotFoundError:
    install("discord.py-self")
    install("colorama")
    install("asyncio")
    install("requests")


version = "v1.0"
name = f"LoggerCord {version}"
print(
    Fore.BLUE + f"""

    █░░ █▀█ █▀▀ █▀▀ █▀▀ █▀█ █▀▀ █▀█ █▀█ █▀▄
    █▄▄ █▄█ █▄█ █▄█ ██▄ █▀▄ █▄▄ █▄█ █▀▄ █▄▀ {version}
    """
)

print(Fore.WHITE + "By Vp \n")
print(f"{name} Logging messages: ")        



@client.event
async def on_message(message):
    await asyncio.sleep(2)
    
    image = "/image"
    now = datetime.datetime.now()
    now = now.strftime("%d-%m-%y %H:%M:%S")
    m = str(message.content)
    a = str(message.author)

    for att in message.attachments:
        attachment = att.get("url").lower()
        filename = attachment.split('/')[-1]
        if isinstance(message.channel, discord.abc.PrivateChannel):
            if filename.find(".png") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".png", 'wb').write(r.content)
            if filename.find(".jpg") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".jpg", 'wb').write(r.content)
            if filename.find(".gif") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".gif", 'wb').write(r.content)
            if filename.find(".mp4") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".mp4", 'wb').write(r.content)
            if filename.find(".mov") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".mov", 'wb').write(r.content)
            if filename.find(".webm") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".webm", 'wb').write(r.content)
            if filename.find(".txt") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open('./loggercord/image/'+a+" - " +
                     now+".txt", 'wb').write(r.content)
        else:
            s = message.guild.name
            if filename.find(".png") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".png", 'wb').write(r.content)
            if filename.find(".jpg") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".jpg", 'wb').write(r.content)
            if filename.find(".gif") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".gif", 'wb').write(r.content)
            elif filename.find(".mp4") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".mp4", 'wb').write(r.content)
            elif filename.find(".mov") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".mov", 'wb').write(r.content)
            elif filename.find(".webm") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".webm", 'wb').write(r.content)
            elif filename.find(".txt") != -1:
                r = requests.get(attachment, allow_redirects=True)
                open(s + '/image/'+a+" - "+now+".txt", 'wb').write(r.content)
    # check if message has an attachment, if it does save it and print the url
    if message.attachments:
        # loggercord
        if isinstance(message.channel, discord.abc.PrivateChannel):
            # create folders
            createFolder("loggercord")
            createFolder("loggercord"+image)
            # print logged message & attachment URL.
            maintsr = now + "(PM) " + str(a) + ': ' + \
                str(m) + " " + att.get("url")
            print(maintsr)
            # write logged message & attachemnt URL to file
            writepath = "loggercord/loggercord.txt"
            mode = 'a' if os.path.exists(writepath) else 'w'
            aaa = open(writepath, mode, encoding='utf-8')
            aaa.write(maintsr + '\n')
            aaa.close()
        # guilds
        else:
            s = str(message.guild.name)
            c = str(message.channel.name)
            # create folders
            createFolder(s)
            createFolder(s+image)
            e = ".txt"
            # print logged message & attachment URL.
            maintsr = "["+now+"] "+"(" + message.guild.name + "/" + message.channel.name + \
                ") " + str(a) + ': ' + str(m) + " " + att.get("url")
            print(maintsr)
            # write logged message & attachemnt URL to file
            writepath = s + "/" + s + e
            mode = 'a' if os.path.exists(writepath) else 'w'
            text_file = open(writepath, mode, encoding='utf-8')
            text_file.write(maintsr + '\n')
            text_file.close()
    # no attachments:
    else:
        # loggercord
        if isinstance(message.channel, discord.abc.PrivateChannel):
            # print logged message
            maintsr = "["+now+"] "+"(PM) " + str(a) + ': ' + str(m)
            print(maintsr)
            # create folders
            createFolder("loggercord")
            createFolder("loggercord"+image)
            # write logged messages to file
            writepath = "loggercord/loggercord.txt"
            mode = 'a' if os.path.exists(writepath) else 'w'
            aaa = open(writepath, mode, encoding='utf-8')
            aaa.write(maintsr + '\n')
            aaa.close()
        # guilds
        else:
            s = message.guild.name
            c = message.channel.name
            f = s
            # create folders
            createFolder(s)
            createFolder(s+image)
            # print logged message
            maintsr = "["+now+"] "+"(" + message.guild.name + "/" + \
                str(c) + ") " + str(a) + ': ' + str(m)
            print(maintsr)
            # write logged messages to file
            e = ".txt"
            writepath = f + "/" + s + e
            mode = 'a' if os.path.exists(writepath) else 'w'
            text_file = open(writepath, mode, encoding='utf-8')
            text_file.write(maintsr + '\n')
            text_file.close()


client.run(token)
