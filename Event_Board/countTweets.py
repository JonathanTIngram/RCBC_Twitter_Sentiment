import openFiles
import tweepy

apiKey = openFiles.OpenFiles.openApiKey()
apiSecretKey = openFiles.OpenFiles.openApiSecretKey()

accessToken = openFiles.OpenFiles.openAccessToken()
accessTokenSecret = openFiles.OpenFiles.openAccessTokenSecret()

auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
auth.set_access_token(accessToken,accessTokenSecret)

api = tweepy.API(auth)

def buildTestSet(search_keyword):
    try:
        tweets_fetched = api.search(search_keyword, count = 100)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

buildTestSet("#RCBCsteam")