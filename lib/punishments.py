# -*- coding: utf-8 -*-

import re
from random import randint

bbcode_regex = re.compile("\[.+?\]")

def scenify(redis, cookie, chat, line):
    replacements = [
        ["color", "I AM BAD AND TRIED TO ESCAPE"],
        ["font", "I AM BAD AND TRIED TO ESCAPE"],
        [":)", "xD"],
        [":(", "DX"],
        ["lol", "LOLZ o◖(≧∀≦)◗o"],
        [":3", "x3"],
        ["you", "u"],
        ["omg", "ZOMGZ!!11"],
        ["omfg", "oh my freaking gog!! xD"],
        ["oh my god", "oh my gob"],
        ["she", "her"],
        ["he", "him"],
        ["have", "has"],
        ["my", "mah"],
        ["im done", "RAWR MEANS I LOVE YOU IN DINOSAUR!"],
        ["im so done", "RAWR MEANS I LOVE YOU IN DINOSAUR!"],
        ["i’m done", "RAWR MEANS I LOVE YOU IN DINOSAUR!"],
        ["shit", "poopies~"],
        ["holy poopies~", "I’M SO RANDOM"],
        ["love", "l"],
        ["me", "meh"],
        ["christ", "WHAT’S YOUR MYSPACE? XD maybe we can be bffs!!(warning i have a LOT of random music on mine."],
        ["fuck", "fudge"],
        ["hell", "heck"],
        ["damn", "darn"],
        ["ass", "booty"],
        ["haha", "mwahahaha!!!111"],
        ["what", "wat"],
        ["bye", "baiiii XD"],
        ["hello", "hallo! xD"],
        ["hate", "haterz gunna h8"],
        ["help", "halpz me"],
        ["jfc", "jegus fudging crust"],
        ["admins", "those cool guys"],
        ["sorry", "sawwy"],
        ["i’m sawwy", "I apologize to the MSPARP staff for being a little shit. Please don’t ban me. [color=#eeeeee] haha your pain is funny[/color]"],
        ["im sawwy", "I apologize to the MSPARP staff for being a little shit. Please don’t ban me. [color=#eeeeee] haha your pain is funny[/color]"],
        ["okay", "otay"],
        ["ok", "okayz"],
        ["brb", "AHLL BE BAC >:DDDD MWAHAHAHA"],
        ["later", "laterz!!1"],
        ["please", "plz"],
        ["no", "noes"],
        ["oc", "original character (mine dnt stealzies)"],
        ["stop", "staph"],
        ["its", "itz"],
        ["it’s", "it’z"],
        ["wow", "wowzers"],
        ["seen", "sce[i][/i]ne"],
        ["crying", "THE FEELS! I’M CRYING IRL \◖(,◕ д ◕, )◗/"],
        ["scene", "not emo"],
        ["fudge u", "fak u ◖(◕◡◕)◗凸"],
        ["the feels", "oh glob i’m crying my mascara is running. it makes me look like a panda XD"],
        ["the", "teh"],
        ["yes", "yiff meh"],
        ["wait", "w8"],
        ["is", "iz"],
        ["bad", "bed"],
        ["bulge", "hentai tentacles!"],
    ]

    r = lambda: randint(0, 255)
    color = '%02X%02X%02X' % (r(), r(), r())

    # Lower case quirk.
    line = line.lower()

    # Replacements.
    for replacement in replacements:
        line = line.replace(replacement[0].decode('utf-8', 'ignore'), replacement[1].decode('utf-8', 'ignore'))

    # Prefix
    line = "[font=Comic Sans MS] [color=#%s] k1nqp4ndA: ◖(◕ω◕)◗ < %s".decode('utf-8', 'ignore') % (color, line)

    # Redis stuffs.
    datakey = 'session.%s.chat.%s' % (cookie, chat)
    redis.hset(datakey, 'color', color)
    redis.hset(datakey, 'acronym', '')
    redis.hset(datakey, 'name', 'XxTEH PANDA KINGxX')
    redis.hset(datakey, 'quirk_prefix', '')

    return line[:1500]

def balon(redis, cookie, chat, line):
    replacements = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        "h": "....",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        '(': "-.--.-",
        ')': "-.--.-",
        ",": "--..--",
        "?": "..--..",
        "/": "-..-.",
        "\"": ".-..-.",
        "=": "-...-",
        "@": ".--.-.",
        ".": ".-.-.-",
        "-": "-....-",
        "'": ".----.",
        " ": "/"
    }

    # Lower case quirk.
    line = line.lower()

    # Strip BBCode to prevent sneakyness.
    line = bbcode_regex.sub("dingleberry", line)

    # Replacements
    morse = ""
    for x in line:
        try:
            morse += replacements[x] + " "
        except KeyError:
            pass

    # Prefix
    line = u'~O %s' % (morse)

    # Redis
    datakey = 'session.%s.chat.%s' % (cookie, chat)
    data = {
        'case': 'lower',
        'replacements': '[]',
        'name': 'inflatedRaisin',
        'color': '35a9b8',
        'acronym': '',
        'quirk_prefix': ''
    }
    redis.hmset(datakey, data)

    return line[:1500]
