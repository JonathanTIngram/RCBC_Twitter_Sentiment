#Jonathan Ingram
#12/20/2019
#define differnt types of posts



'''
PLEASE READ:

The primary purpose of this file is to define and catagorize
different types of twitter post
Nothing will be run directly in this file.

'''
#External Libraries
import random
import time
from time import strftime
import tweepy
import textblob

import openFiles

#Reading in keys
apiKey = openFiles.OpenFiles.openApiKey()
apiSecretKey = openFiles.OpenFiles.openApiSecretKey()

accessToken = openFiles.OpenFiles.openAccessToken()
accessTokenSecret = openFiles.OpenFiles.openAccessTokenSecret()

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)


#Posts class
class Posts:
    def __init__(self):
        print("Instance of posts class within PostTypes.py")

    def tweetImage():
        media = api.media_upload("Images/mountain.jfif")

        post_result = api.update_status(status="Chill:\n\n\n", media_ids=[media.media_id])

    def onePost():
        api.update_status(status="test")

    def hourlyPost():

        
        def getTime():                      #Gets the time and retruns as a string
            string = strftime('%H:%M:%S') 
            print(string)
            return string

        hour = 0
        checkHour = ":33:30"
        postTime = ""

        
        while (postTime != "11:30:30"): #loop until it's 11:30 pm
            timeString = str(getTime())
            print(timeString)
            time.sleep(1)


            #Definatly a better way to do this, just got lazy
            postTime = timeString[2] + timeString[3] + timeString[4] + timeString[5] + timeString[6] + timeString[7]

            if(postTime == checkHour):
                Posts.onePost()


''' 
#Functions that are TBD to be put into production
    def nounVerbNoun():
        

        nvn = openFiles.OpenFiles.getNoun() + openFiles.OpenFiles.getVerb() + openFiles.OpenFiles.getNoun()
        print(nvn)
        #api.update_status(status=nvn)

    def pastTenseNounVerbNoun():

        nPTVn = "The\n" + openFiles.OpenFiles.getNoun() + openFiles.OpenFiles.getPastTenseVerb().lower() + "the\n" +  openFiles.OpenFiles.getNoun()

        print(nPTVn)

    def nameVerbNoun():

        nPTVn = openFiles.OpenFiles.getName() + openFiles.OpenFiles.getPastTenseVerb().lower() + "the\n" +  openFiles.OpenFiles.getNoun()

        print(nPTVn)

    def newMeme():


        memeCheck = True
        while (memeCheck == True):

            nMeme = openFiles.OpenFiles.getMeme()
            print(nMeme)

            memeCheck = True
            answer = input("Do you like this meme? ")

            if (answer == "y"):
                print("posted")
                api.update_status(status=nMeme)
                memeCheck = False

            else:
                print("not posted")
'''

#End of Posts classs