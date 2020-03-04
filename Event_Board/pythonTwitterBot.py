#Jonathan Ingram
#12/10/2019
#Twitter Bot for RCBC Foundation Ceremony

'''
PLEASE READ:

This is the primary program of this project.
Any data being displayed should be executed within this file.

'''
#Exernal Libraries
import tweepy
import time
from time import strftime
import random
from random import randint

import openFiles
import PostTypes


if __name__ == "__main__":
   PostTypes.Posts.tweetImage()