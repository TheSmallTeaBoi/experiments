# Importing things
from pypresence import Presence

import random, json, time, asyncio

# Here we open the json file with all the strings
def importData(file):
    loadedFile = open(file)
    data = json.load(loadedFile)
    return data

def exitApp(error):
    print('[ERROR]' + error)

statusFile = 'statusList.json'
linksFile = 'linkList.json'
imagesFile = 'imagesList.json'
phrasesFile = 'phrasesList.json'
configFile = 'config.json'

config = importData(configFile)


# This is the client ID, you can change it in config.json
token = config["token"]

# Here you uh do things?
RPC = Presence(token)
try:
    RPC.connect()
    print('Rich Presence connected succesfully!')
except ConnectionRefusedError or AssertionError:
    print('[ERROR] Something went wrong while trying to connect to Discord, is Discord open?\n')
    exit

# thing kind of uh does things too
prevCycles = 0

# This is what updates the rich presence
while True:
    # Updating the data so you don't have to re-run the 
    # script when you add new things
    statusList = importData(statusFile)
    linksList = importData(linksFile)
    imagesList = importData(imagesFile)
    phrasesList = importData(phrasesFile)
    config = importData(configFile)

    # Run once every two loops
    if prevCycles == 3 or prevCycles == 0:
        bigImage = random.choice(imagesList)
        bigImageText = 'Theo says: "' + random.choice(phrasesList) + '"'
        prevCycles = 1

    # Here we define what will displayed
    smallImage = 'heart'
    smallImageText = config["smallImageText"]
    mainText = config["mainText"]
    smallText = random.choice(statusList)
    buttonText = config["buttonText"]
    buttonURL = random.choice(linksList)


    # Here is where we actually update the rich presence, with some kind of
    # slight error handling
    try:
        RPC.update(
        large_image = bigImage,
        large_text = bigImageText,
        small_image = smallImage,
        small_text = smallImageText,
        details = mainText,
        state = smallText,
        buttons=[{"label":buttonText, "url":buttonURL}]
        )
    except ConnectionRefusedError or AssertionError:
        print('[ERROR] Something went wrong while trying to connect to Discord, is Discord open?\n')
        exit

    prevCycles += 1

    # And we wait a little before updating again
    time.sleep(30)
