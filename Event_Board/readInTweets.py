#Jonathan Ingram
#2/18/2020
#Read in Tweets and store in tweets.txt


import tweepy
import textblob
from textblob import TextBlob
import openFiles
import json
import os
import pandas as pd

#Reading in keys
apiKey = openFiles.OpenFiles.openApiKey()
apiSecretKey = openFiles.OpenFiles.openApiSecretKey()

accessToken = openFiles.OpenFiles.openAccessToken()
accessTokenSecret = openFiles.OpenFiles.openAccessTokenSecret()

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)

public_tweets = api.search('Rowan College at Burlington County')



  
  
# Function to extract tweets 
def get_tweets(username): 
          
  
        # 200 tweets to be extracted 
        number_of_tweets = 1
        tweets = api.user_timeline(screen_name=username) 
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created  
        for j in tweets_for_csv: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(j)
            tmp.append("\n")  


            #for tweet in public_tweets:    
            #   print(tweet.text)   
    
            analysis = TextBlob(str(tmp))    
            print(analysis.sentiment)    

            if analysis.sentiment[0]>0:
                print("\n")
                print(analysis.sentiment)       
                print('\nThis Tweet is Positive\n\n\n') 

                tmp.append(str(analysis.sentiment))
                tmp.append('\nThis Tweet is Positive\n\n\n')   
            elif analysis.sentiment[0]<0:  
                print("\n")
                print(analysis.sentiment)     
                print('\nThis Tweet is Negative\n\n\n') 

                tmp.append(str(analysis.sentiment)) 
                tmp.append('\nThis Tweet is Negative\n\n\n')  
                
            else:       
                print('\nThis Tweet is Neutral\n\n\n')
                tmp.append('\nThis Tweet is Neutral\n\n\n')
  
        # Printing the tweets 
        print(tmp) 

        with open("tweets.txt", "w") as t:
            t.writelines(tmp)

  
def searchTweetByHashtag(hashtag):

    date_since = "2020-03-03"
        
    tweets = tweepy.Cursor(api.search, q=hashtag, lang="en",
                since=date_since).items(2)

    tmp=[] 

    for tweet in tweets:
        #print(str(tweet).split(","))
        print(str(tweet))

        print(tweet.text)
        print("\n\n")
        tmp.append(tweet)
        tmp.append(tweet.text)


    with open("test.json", "w") as write_file:
        json.dump(str(tmp), write_file)
  
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    searchTweetByHashtag("#RCBCsteam")  



#Credit to FreeCodeCamp


