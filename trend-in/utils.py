# basic utilities
import json
import tweepy
import re

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


def get_config():
    """ read configuration and load into a json object """
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
            return config
    except IOError as err:
        print("OS error: {0}".format(err))


def get_logger():
    """ return a logger for all modules """
    return None


def get_twitter_auth():
    config = get_config()
    auth = OAuthHandler(
        config["twitter"]["consumer_key"], config["twitter"]["consumer_secret"])
    auth.set_access_token(
        config["twitter"]["access_token"], config["twitter"]["access_token_secret"])
    return auth


def get_twitter_api():
    api = tweepy.API(get_twitter_auth())
    return api


class UrlListener(StreamListener):

    """
    This is a basic listener that just prints received tweets to stdout.
    My listener needs to print only the time, text, tweet_id, user, if it's
    a retweet .. and source user if its a retweet
    """

    def on_data(self, status):
        pattern_url = re.compile(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        data = json.loads(status)
        # I am interested in id, created_at, screen_name, location,
        # in_reply_to_source_id, in_reply_to_screen_name, text
        if(pattern_url.match(data['text'])):
            print("\t".join([data['id_str'], data['created_at'], data['user'][
                  'screen_name'], data['user']['location'], data['text']]))
        return True

    def on_error(self, status):
        print(status)
