from slackbot.bot import respond_to
from slackbot.bot import listen_to
import os
import re
import socket
import urllib
import json

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@listen_to('Can someone help me?')
def help(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')

    # Message is sent on the channel
    # message.send('I can help everybody!')

@respond_to('Give me (.*)')
def giveme(message, something):
    message.reply('Here is %s' % something)

@listen_to("!temp")
def temp(message):
    temp = float(getTemp())
    message.reply("Temp currently: %s'C" % temp)

@listen_to("!ip")
def ip(message):
    message.reply("Internal IP: %s" % getInternalIP())
    message.reply("External IP: %s" % getExternalIP())
    
@listen_to("!number")
def number(message):
    import random
    message.reply(random.randint(0, 9))
    
@listen_to("!random")
def random(message):
    message.reply(getRandomLyric())

@listen_to("!joke")
def joke(message):
    message.reply(getJoke())

def getTemp():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getInternalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def getExternalIP():
    site = urllib.urlopen("http://icanhazip.com").read()
    return site
    
def getRandomLyric():
    import random
    lyrics = [
        "Yeah yeah yeah I'm still about (TEMPZ!!!)",
        "Don't watch the hype (MAD! NEXT HYPE!)",
        "This is for my fans dem, you get me? (NEXT HYPER TUNE!)",
        "Man's still spitting, it's a ting you get me...",
        "What kind of things that you have",
        "When I find out don't expect me to stop",
        "I'll come for the P's that you stack",
        "And come for all the food that you blot",
        "Better hand over the bag",
        "Your boys don't wanna see you shot",
        "If I kick down the door to your flat",
        "Dun Know I'll clear out your house on the spot",
        "(CLEAR!) All the things in your house",
        "(CLEAR!) All the things in your fridge",
        "(SMASH!) All your plates from your rack",
        "(CLEAR!) All'a your kids' toys",
        "(CLEAR!) All'a your CD rack",
        "Won't get none of your CD's back",
        "Drag off your curtain rail from the wall",
        "Kick off your HDTV from the stand",
        "Run up on stairs into rooms",
        "Flip the mattress and search for the cash",
        "Make man look down the barrel of a mash",
        "It's not worth your life, just cough up the scratch",
        "It's too late to lock up the latch",
        "I can smell the crow, just pull out the batch",
        "I'm not here to cotch or relax",
        "And drink your wine here just pull out the bags",
        "I have to punch up guys",
        "Guys try it with me, I don't know why",
        "Bax! Pax man straight in his eyes",
        "They floored me, I was looking at the sky",
        "Par! Now I have to go blind",
        "That boy there I swear he gonna die",
        "You're not bad you're a mug don't think you're a guy",
        "When I slap man you won't be alright",
        "Catch man on the field flying his kite",
        "Roll man down on the grass with a knife",
        "Watch as his friends disperse out of sight from afar",
        "I can hear screams from his wife",
        "Run after man let me draw for his life",
        "Blood's pouring I got stains off the knife",
        "Leave guys dead in the field over night",
        "I'm sick, when I dream I won't think of them twice",
        "What d'you know about the All Star pars?",
        "Don't wanna see man driving his car",
        "I'm behind tints with the leng in the car",
        "I jumped out the car put the leng to his car",
        "I said 'get out the CAR!'",
        "I said 'this ain't a PAR!'",
        "Smash the window, drag man out the car",
        "(DRAPES!) Get out the car!",
        "If you don't get out the car",
        "Don't wanna see man shooting at star",
        "You better not dare me now",
        "I don't care if you got friends in your car",
        "Light up your whip and all of your spars",
        "Watch some of them roll out of the car",
        "Run down the road I'm chasing them far",
        "Why didn't they comply from the start",
        "Tryna hype up on the mic",
        "While I spray my bars on the mic",
        "(SLAP!) Don't hype up on the mic",
        "(KICK!) Now who here wants to fight",
        "Strangle man with the microphone lead",
        "Bax mans head with the side of the mic",
        "Shout at mans face I'm not taking it light",
        "Drag man down to the floor thats right",
        "Pulling out lengs everywhere",
        "Dun kno we got the shotgun there",
        "Boy man down from the side of the stairs",
        "See that man tryna run over there",
        "Run after man chase man over there",
        "Hop the railings chase man over there",
        "WOYYYY! Straight over there",
        "I locked on the sight now yout's down there",
        "So I jumped downstairs",
        "Now who here wants to fuck around in here",
        "Stay down, keep your head to the ground",
        "Dun know I'll shoot off your headtop clear",
        "No, it was a war last year",
        "This year it's kicking off right here",
        "This year it's kicking off right here",
        "Dun know we got the shotgun there",
        "If I go make me a mask",
        "No one see who boyed off the ting",
        "Run up on man I'll boy off the ting",
        "Hop the railings and boy off the ting",
        "WOYYYY! Make me a mask",
        "No one see who boyed off the ting",
        "Run out the bush and boy off the ting",
        "You're screaming please don't boy off the ting!",
        "Are you fucking mad? Next hype",
        "What everyone's asking me when's the next tune?",
        "This is the fucking next tune, are you dumb?",
        "Next hype, Slew Dem, free Chronik you mad?",
        "Big up Esco, Rage, Shorty Smalls. Slewww demmmm. 09"
    ]
    return random.choice(lyrics)

def getJoke():
    joke = json.loads(urllib.urlopen("http://api.icndb.com/jokes/random?firstName=Tempa&lastName=T").read())
    return joke['value']['joke']


