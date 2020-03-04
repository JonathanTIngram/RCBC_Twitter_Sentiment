import openFiles
import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt 
import time
import os
import sys

#Reading in keys
apiKey = openFiles.OpenFiles.openApiKey()
apiSecretKey = openFiles.OpenFiles.openApiSecretKey()

accessToken = openFiles.OpenFiles.openAccessToken()
accessTokenSecret = openFiles.OpenFiles.openAccessTokenSecret()

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)



date_since = "2020-03-03"

''' 
You can restrict the number of tweets returned
 by specifying a number in the .items() method. .
 items(5) will return 5 of the most recent tweets.

 tweepy.Cursor(api.search, q=hashtag, lang="en",
                since=date_since, include_entries=False).items(2)

'''
def searchTweetByHashtag(hashtag):

    tweets = tweepy.Cursor(api.search, q=hashtag, lang="en",
                since=date_since, include_entries=False).items(2)

    tmp=[] 

    for tweet in tweets:
        print(tweet)
        print(tweet.text)
        print("\n\n")
        tmp.append(tweet)
        tmp.append(tweet.text)


    with open("test.json", "w") as write_file:
        json.dump(str(tmp), write_file)



if __name__ == '__main__': 
    searchTweetByHashtag("#RCBCsteam")