#!/usr/bin/env python3

import pywhatkit
import contacts



def sendmsg(name, msg):
    local_numbers = contacts.numbers
    pywhatkit.sendwhatmsg(local_numbers[name], msg, 8, True, 5)

def sendmsginstant(name, msg):
    local_numbers = contacts.numbers
    pywhatkit.sendwhatmsg_instantly(local_numbers[name], msg, 8, True, 5)

def sendtogroup(groupName, msg):
    local_group = contacts.groups
    pywhatkit.sendwhatmsg_to_group(local_group[groupName], "something", 18, 32, 10, False)


def sendimg(groupOrNumber, pathToImg, imgMsg):
    local_numbers = contacts.numbers
    local_groups = contacts.groups
    try:
        pywhatkit.sendwhats_image(local_numbers[groupOrNumber], pathToImg, imgMsg, 10, True, 5)
    except:
        pywhatkit.sendwhats_image(local_groups[groupOrNumber], pathToImg, imgMsg, 10, True, 5)

sendtogroup("Nokepa", "test")
