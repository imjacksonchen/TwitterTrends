# TwitterTrends/config.py
# This python file sets up our API for use

import tweepy
import logging
import os

logger = logging.getLogger()

def createAPI():

    # os.getenv will get the envrionment variable that corresponds to the vairable name.
    # This is to prevent from your secret strings from going public.
    # To set this up on linux/mac OS, for example, the command to set up CONSUMER_KEY
    # The command is: export CONSUMER_KEY="Your secret strings here"

    consumerKey = os.getenv("CONSUMER_KEY")
    consumerSecret = os.getenv("CONSUMER_SECRET")
    accessToken = os.getenv("ACCESS_TOKEN")
    accessTokenSecret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessTokenSecret)
    
    api = tweepy.API(auth, wait_on_rate_limit = True,
        wait_on_rate_limit_notify = True)

    try:
        api.verify_credentials()
    except Exception as error:
        logger.error("Error creating API", exc_info = True)
        raise error
    
    logger.info("API created")
    return api