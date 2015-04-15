# basic utilities
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


def get_config():
    try:
        with open('../config.json') as config_file:
            config = json.load(config_file)
            # print(config["twitter"]["consumer_key"])
            return config
    except IOError as e:
        print("OS error: {0}".format(err))


def get_logger():
    return None


def get_auth():
    config = get_config()
    auth = OAuthHandler(
        config["twitter"]["consumer_key"], config["twitter"]["consumer_secret"])
    auth.set_access_token(
        config["twitter"]["access_token"], config["twitter"]["access_token_secret"])
    return auth


def get_twitter_api():
    api = tweepy.API(get_auth())
    return api

# This is a basic listener that just prints received tweets to stdout.


class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == "__main__":
    # get_config()
    # api = get_twitter_api()
    # print(api.verify_credentials())
    listener = StdOutListener()
    auth = get_auth()
    stream = Stream(auth, listener)
    stream.filter(track=["india"])
