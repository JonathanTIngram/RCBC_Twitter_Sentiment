#Jonathan Ingram
#2/20/2019
#Open files for the Twitter bot


''' 
PLEASE READ:

The Primary purpose of this file is to read in text documents
Nothing will run directly in this file
'''

#External Libraries
import random


#Open Files Class
class OpenFiles:
    def __init__(self):
        print("File Openings")


    #API keys

    def openApiKey(): #Opens API key from a text document

        with open("Keys/apiKey.txt", "r") as a:
            apiKey = a.read()

        return apiKey

    def openApiSecretKey(): #Opens API Secrect Key from text document

        with open("Keys/apiSecretKey.txt", "r") as b:
            apiSecretKey = b.read()

        return apiSecretKey

    def openAccessToken(): #Opens Access Token from text document

        with open("Keys/accessToken.txt", "r") as c:
            accessToken = c.read()

        return accessToken

    def openAccessTokenSecret(): #Opens Access Token Secret from text document

        with open("Keys/accessTokenSecret.txt", "r") as d:
            accessTokenSecret = d.read()

        return accessTokenSecret


    


    ''' 
    
    Testing reading in differnt files for sentence generator.
    
    '''
    def getNoun():
        with open("Text/nouns.txt", "r") as n:
            nouns = n.readlines()

        noun = random.choice(nouns)

        return noun

    def getVerb():
        with open("Text/verbs.txt", "r") as v:
            verbs = v.readlines()

        verb = random.choice(verbs)

        return verb

    def getPastTenseVerb():

        with open("Text/pastTenseVerbs.txt", "r") as ptv:

            pastTensev = ptv.readlines()

        PTV = random.choice(pastTensev)

        return PTV

    def getName():
        
        with open("Text/names.txt", "r") as na:
            names = na.readlines()

        name = random.choice(names)

        return name

    
    def getMeme():

        with open("Text/memeWords.txt", "r") as m:
            memes = m.readlines()

        meme = random.choice(memes) + random.choice(memes)

        return meme

    def readInTweets():

        with open("Text/tweets.txt", "r") as t:
            tweets = t.readlines()

#End of Open Files Class

    

