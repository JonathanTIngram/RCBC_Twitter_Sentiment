from tweepy import API
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import pandas

import openFiles

class TwitterStreamer():
    #Processes live tweets

    def stream_tweets(self, fetched_tweets_filename, hashtag_list):
        #Handles Twitter authentication and Twitter Streaming

        listener = TwitterListener(fetched_tweets_filename)
        auth = OAuthHandler(openFiles.OpenFiles.openApiKey(),
                openFiles.OpenFiles.openApiSecretKey())
        auth.set_access_token(openFiles.OpenFiles.openAccessToken(),
                                openFiles.OpenFiles.openAccessTokenSecret())


        stream = Stream(auth, listener)

        stream.filter(track=hashtag_list)

class TwitterListener(StreamListener):
    #listens for tweets


    def __init__(self, fetch_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):

        try:

            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True

        except BaseException as e:

            print("Error on_data: %s " % str(e))
        return True

    def on_error(self, status):
        
        print(status)



if __name__ == "__main__":

    hashtag_list = ["RCBCsteam"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hashtag_list)


