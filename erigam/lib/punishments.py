# -*- coding: utf-8 -*-

import re
import random
import json

bbcode_regex = re.compile("\[.+?\]")

def punish(redis, cookie, chat, line):
    word_regex = re.compile("[^a-zA-Z\s]+")
    bbcode_regex = re.compile("\[.+?\]")
    replacements = [
        ["nigglet", "^o^ frienddsss"],
        ["jew", "panda"],
        ["kike", "panda"],
        ["gamzee", "gamzette"],
        ["aradia", "aradio"],
        ["tavros", "tavvie"],
        ["sollux", "sollie"],
        ["nepeta", "nepeto"],
        ["terezi", "jersey shore"],
        ["kanaya", "kanmayo"],
        ["vriska", "vrisko"],
        ["karkat", "kitkat"],
        ["equius", "equiqui"],
        ["eridan", "wweh nyeh 4ever alone boi"],
        ["feferi", "ferrari"],
        ["jane", "john w/ boobs"],
        ["john", "joan"],
        ["dave", "dove"],
        ["jake", "jo[i][/i]n"],
        ["dirk", "diva"],
        ["rose", "ross"],
        ["jade", "jude"],
        ["noncon", "poo"],
        ["no ", "yiff my anus <3 "],
        ["kankri", "karkles"],
        ["damara", "weeaboo queen :o"],
        ["rufioh", "ROOFIOOOOOOOOOOOOH"],
        ["mituna", "precious baby tutu"],
        ["meulin", "nepe[i][/i]ta"],
        ["latula", "tu tu babes ugly gf(im getting rid of her XD)"],
        ["aranea", "other vrisk[i][/i]a"],
        ["horuss", "horse"],
        ["cronus", "nyehhhh greasar XD"],
        ["meenah", "mean fefe[i][/i]ri"],
        ["dildo", "no no stick =-="],
        ["roxy", "roxayyyyy"],
        ["your", "you'[i][/i]re"],
        ["you're", "yo[i][/i]ur"],
        ["[color", "<BBCODE REMOVED xD>"],
        ["[font", "<BBCODE REMOVED xD>"],
        ["color", "colarz"],
        ["colour", "coularz"],
        ["y e s", "BURRITO!!!"],
        ["ye s", "PANCAKE MIXS"],
        ["fuckass", "featherduster"],
        ["homestuck", "homestuck ＼(=^‥^)/’"],
        ["y es", "i once tried dying my hair but it goes back to teh pinks because it no likeys the blue"],
        ["b i t c h", "grrrz (◞≼◉ื≽◟ ;益;◞≼◉ื≽◟)Ψ"],
        ["a s s", "poo poo hole"],
        ["stink", "stinkay"],
        [":)", "xD"],
        [":(", "DX"],
        ["them", "thems"],
        ["like", "likeys"],
        ["f u c k", "FIDDLY DIDDLY!"],
        ["f u ck", "frickle de doo"],
        ["fu ck", "yiff me hard"],
        ["fuc k", "f*** (sorry for the foul language)"],
        ["f uck", "i like pants"],
        ["y.e.s", "yiff my furry ass"],
        ["fuc k", "frideg"],
        ["f uc k", "pole benders!!!"],
        ["fu c k", "P I Z Z A"],
        ["lol", "LOLZ o◖(≧∀≦)◗o"],
        [":3", "x3"],
        ["you", "u"],
        ["yaoi", "teh yaois (dont like dont read)"],
        ["omg", "ZOMGZ!!11"],
        ["yo ", "im a gangzters"],
        ["nipple", "tinkle winkle"],
        [" hey", "hay"],
        ["fuck off", "my pits smell like applesauce with cream cheese!"],
        ["omfg", "oh my freaking gog!! xD"],
        ["oh my god", "oh my gob"],
        ["she", "her"],
        ["have", "has"],
        ["my", "mah"],
        ["im done", "RAWR MEANS I LOVE YOU IN DINOSAUR!"],
        ["im so done", "RAWR MEANS I LOVE YOU IN DINOSAUR!"],
        ["shit", "poopies~"],
        ["holy poopies~", "I'M SO RANDOM"],
        ["love", "LUrve"],
        ["what?", "[O___________0]< AWKWARD WHALE HERE to ask: r u highs XD"],
        ["me", "meh"],
        ["christ", "WHAT'S YOUR MYSPACE? XD maybe we can be bffs!!(warning i have a LOT of random music on mine."],
        ["fuck", "fudge"],
        ["damn", "darn"],
        ["ass", "booty"],
        ["haha", "mwahahaha!!!111"],
        ["what", "wat"],
        ["bye", "baiiii XD"],
        ["hello", "hallo! xD"],
        ["hate", "LOVE"],
        ["hell", "heck"],
        ["help", "halpz me"],
        ["jfc", "jegus fudging crust"],
        ["admins", "those cool guys"],
        ["sorry", "sawwy"],
        ["im sawwy", "I apologize to the MSPARP staff for being a little shit. Please don't ban me. [color=#eeeeee] haha your pain is funny[/color]"],
        ["okay", "otay"],
        ["ok", "okayz"],
        ["idk", "i dun knoes"],
        ["brb", "AHLL BE BAC >:DDDD MWAHAHAHA"],
        ["later", "laterz!!1"],
        ["please", "plz"],
        ["oc ", "original character (mine dnt stealzies)ლ(=ↀωↀ=)ლ"],
        ["special", "speshul"],
        ["stop", "staph "],
        ["its", "itz"],
        ["wow", "wowzers"],
        ["seen", "sce[i][/i]ne"],
        ["im crying", "THE FEELS! I'M CRYING IRL \◖(,◕ д ◕, )◗/"],
        ["scene", "not emo"],
        ["fudge u", "fak u ◖(◕◡◕)◗凸"],
        ["the feels", "oh glob i'm crying my mascara is running. it makes me look like a panda XD"],
        ["the", "teh"],
        ["yes", "yiff meh"],
        ["wait", "w8"],
        ["is", "iz"],
        ["thrust", "pee"],
        ["want", "wantzies"],
        ["eheh", "pee on the floor"],
        ["hehe", "TEHEHEHE X3"],
        ["bad", "badzies o-O"],
        ["bulge", "hentai tentacles! ༼ꉺ౪ꉺ༽"],
        ["kill", "huuuggggg (ﾉ≧∀≦)ﾉ"],
        ["murder", "tickle"],
        ["die", "be my bff (ﾉ´ヮ´)ﾉ*:･ﾟ✧"],
        ["ddos", "poo aggresively on"],
        ["nigger", "awesome people"],
        ["trans scum", "i am so sorry for everything i've said"],
        ["faggot", "best pal"],
        ["fag ", "CHEESE WHEELS XD"],
        ["suicide", "hug my stuffies"],
        ["nigga", "panda buddies <3"],
        ["a proxy", "a secrat thingy o-O"],
        ["proxy", "teh secrat thing"],
        ["proxies", "my L33T proxay"],
        ["hack", "ship"],
        ["bitch", "karry"],
        ["bootyhole", "karry"],
        ["yesterday", "yiff mehterday"],
        ["sucks", "is the best"],
        ["gay", "rose"],
        ["jesus", "o_o mlp"],
        ["boob", "boobiehz XD"],
        ["dick", "anusfly"],
        ["vagina", "pee pee hole"],
        ["peniz", "pee pee"],
        ["cunt", "meanie bobeanie"],
        ["bugger", "TACOS! XD"],
        ["nazi", "kawaii desu"],
        ["cat", "nepeat"],
        ["jizz", "dinky water"],
        ["cum", "i like potatoes"],
        ["cock", "dingler"],
        ["clit", "winky"],
        ["breast", "breasteses"],
        ["rape", "huggle"],
        ["bbl", "I WILL RETURN XD"],
        ["im fudgeing done", "do you have kik?"],
        ["fudge meh", "let's yiff X3"],
        ["s h i t", "poopsies QAQ"],
        ["hitler", "Tokyo Mew Mew"],
        ["fudge this", "preps never understand QAQ"],
        ["shlong", "pee pee o_o"],
        ["pussy", "tinkler"],
        ["slut", "stinker"],
        ["whore", "big meanie"],
        ["skank", "big doo doo head XO"],
        ["titties", "no no zone"],
        ["owned", "pwned"],
        ["own", "pwn"],
    ]

    try:
        extrapunishments = json.loads(redis.get("panda:additions"))
        replacements = replacements + extrapunishments
    except TypeError:
        pass

    r = lambda: random.randint(0, 255)
    color = '%02X%02X%02X' % (r(), r(), r())

    # Lower case quirk.
    line = line.lower()

    # Strip BBCode and specific non word characters to prevent sneakyness.
    line = bbcode_regex.sub("", line)
    line = word_regex.sub("", line)

    # Replacements.
    for replacement in replacements:
        line = line.replace(replacement[0], replacement[1])

    # Prefix
    line = "[font=Comic Sans MS] [color=#%s] k1nqp4ndA: ◖(◕ω◕)◗ < %s [/color][/font]" % (color, line)

    # Redis stuffs.
    datakey = 'session.%s.chat.%s' % (cookie, chat)
    redis.hset(datakey, 'acronym', '')
    redis.hset(datakey, 'name', 'XxTEH PANDA KINGxX')
    redis.hset(datakey, 'replacements', '[]')
    redis.hset(datakey, 'quirk_prefix', '')

    return line[:1500]
