# Importing things
from pypresence import Presence

import random, json, time, asyncio

# This is the client ID, change it if you want ¯\_(ツ)_/¯
token = '837934057273819147'

# Here you uh do things?
RPC = Presence(token)
RPC.connect()
print('Rich Presence connected succesfully!')



# Here we open the json file with all the strings
def importData(file):
    loadedFile = open(file)
    data = json.load(loadedFile)
    return data

statusFile = 'statusList.json'
linksFile = 'linkList.json'
imagesFile = 'imagesList.json'
phrasesFile = 'phrasesList.json'


# Defining things
def dumpData():
    with open(fileData, 'w') as f:
        json.dump(statusList, f)

# This thing kind of uh does things too
prevCycles = 0

# This is what updates the rich presence
while True:
    # Updating the data so you don't have to rerun the 
    # script when you add new things
    statusList = importData(statusFile)
    linksList = importData(linksFile)
    imagesList = importData(imagesFile)
    phrasesList = importData(phrasesFile)

    # what will be d Here we defineisplayed

    # Run once every two loops
    if prevCycles == 3 or prevCycles == 0:
        bigImage = random.choice(imagesList)
        bigImageText = 'Theo says: "' + random.choice(phrasesList) + '"'
        prevCycles = 1

    smallImage = 'heart'
    smallImageText = 'Have a great day!'
    mainText = 'Theo is currently...'
    smallText = random.choice(statusList)
    buttonText = "Take me to a random place"
    buttonURL = random.choice(linksList)


    # Here is where we actually update the rich presence

    RPC.update(
    large_image = bigImage,
    large_text = bigImageText,
    small_image = smallImage,
    small_text = smallImageText,
    details = mainText,
    state = smallText,
    buttons=[{"label":buttonText, "url":buttonURL}]
    )

    prevCycles = prevCycles + 1

    # And we wait a little before updating again
    time.sleep(30)
