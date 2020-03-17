# WeChat Course Bot

print("WeChat Course Bot\n\nCopyright (C) 2020  Ruixuan Tu\nThis program comes with ABSOLUTELY NO WARRANTY with GNU GPL v3 license. This is free software, and you are welcome to redistribute it under certain conditions; go to https://www.gnu.org/licenses/gpl-3.0.html for details.\n")

from itchat.content import *
from os import path
import datetime
import itchat
import json
import os
import random
import zoom

class GroupInfo:
    lastMessage = ""
    count = 1
    repeatCount = 10
    zoom_confno = ""
    zoom_pwd = ""
    zoom_lastTime = 0

responses = []
whitelist = []
groups = {}
name = ""

def init():
    global responses, whitelist, name
    if not path.exists("response.config.json"):
        f = open("response.config.json", "w")
        f.write("[\"My internet is poor.\",\"I am restarting my router.\",\"My device has no battery now.\"]")
        f.close()
    f = open("response.config.json", "r")
    responses = json.loads(f.read())
    f.close()
    if not path.exists("whitelist.config.json"):
        f = open("whitelist.config.json", "w")
        f.write("[]")
        f.close()
    f = open("whitelist.config.json", "r")
    whitelist = json.loads(f.read())
    f.close()
    if not path.exists("personal.config.json"):
        f = open("personal.config.json", "w")
        f.write("testname")
        f.close()
    f = open("personal.config.json", "r")
    name = f.read()
    f.close()

@itchat.msg_register(TEXT, isFriendChat=False, isGroupChat=True, isMpChat=False)
def receiveGroup(msg):
    if msg.MsgType != 1:
        return
    global responses, whitelist, name, groups
    groupId = 0
    if "@@" in msg.FromUserName:
        groupId = msg.FromUserName
    else:
        groupId = msg.ToUserName
    if len(whitelist) > 0:
        found = False
        for i in whitelist:
            iId = itchat.search_chatrooms(name=i)[0]
            if iId.UserName == groupId:
                found = True
                break
        if found == False:
            return
    if not groupId in groups.keys():
        groups[groupId] = GroupInfo()
        groups[groupId].repeatCount = random.randint(2, 11)
    if str.lower(msg.text) == str.lower(groups[groupId].lastMessage):
        groups[groupId].count = groups[groupId].count + 1
    else:
        groups[groupId].count = 1
        groups[groupId].repeatCount = random.randint(2, 11)
        groups[groupId].lastMessage = msg.text
    print("[MESSAGE] Time: " + datetime.datetime.now().isoformat() + "; Count: " + str(groups[groupId].count) + "; Sender: " + msg.FromUserName + "; Receiver: " + msg.ToUserName + "; Content: " + msg.text)
    if msg.isAt or name in str.lower(msg.text):
        print("[WARNING] You have been mentioned!!!")
        index = random.randint(0, len(responses) - 1)
        print("[RESPONSE] " + responses[index])
        itchat.send(responses[index], groupId)
        return
    if groups[groupId].count == groups[groupId].repeatCount:
        print("[REPEAT] " + msg.text)
        itchat.send(msg.text, groupId)
        return
    if groups[groupId].zoom_lastTime - datetime.datetime.now().timestamp() >= 300:
        groups[groupId].zoom_confno = ""
        groups[groupId].zoom_pwd = ""
    if len(msg.text) >= 9:
        found = False
        for i in range(0, 9):
            if not (msg.text[i] >= '0' and msg.text[i] <= '9'):
                found = True
                break
        if len(msg.text) > 9:
            if msg.text[9] >= '0' and msg.text[9] <= '9':
                found = True
        if found == False:
            groups[groupId].zoom_confno = msg.text[0:9]
            print("[ZOOM] confno: " + groups[groupId].zoom_confno)
            groups[groupId].zoom_lastTime = datetime.datetime.now().timestamp()
            print("[ZOOM] lastTime: " + groups[groupId].zoom_lastTime)
    if len(msg.text) >= 6:
        found = False
        for i in range(0, 6):
            if not (msg.text[i] >= '0' and msg.text[i] <= '9'):
                found = True
                break
        if len(msg.text) > 6:
            if msg.text[6] >= '0' and msg.text[6] <= '9':
                found = True
        if found == False:
            groups[groupId].zoom_pwd = msg.text[0:6]
            print("[ZOOM] pwd: " + groups[groupId].zoom_pwd)
            groups[groupId].zoom_lastTime = datetime.datetime.now().timestamp()
            print("[ZOOM] lastTime: " + groups[groupId].zoom_lastTime)
    if groups[groupId].zoom_confno != "" and groups[groupId].zoom_pwd != "":
        zoom.invoke(zoom.get(groups[groupId].zoom_confno, groups[groupId].zoom_pwd))

init()
itchat.auto_login(hotReload=True)
itchat.run()
