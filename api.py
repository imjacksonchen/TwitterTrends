#!/usr/bin/env python
# TwitterTrends/api.py

import tweepy
import json
from config import createAPI

class TweetStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.retweeted_status:
            return
        print(status.text)

    def on_error(self, statusCode):
        if statusCode == 420:
            return False

if __name__ == "__main__":
    # create instance of the tweepy tweet streamer listener
    streamListener = TweetStreamListener()

    # set twitter keys/tokens
    api = createAPI()

    # create instance of the tweepy stream
    stream = tweepy.Stream(api.auth, streamListener)

    # search twitter for keyword
    stream.filter(track=["fortnite"])