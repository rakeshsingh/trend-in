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
            return config
    except IOError as err:
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
# My listener needs to print only the time, text, tweet_id, user, if it's
# a retweet .. and source user if its a retweet


class LinkListener(StreamListener):

    def on_data(self, raw_data):
        data = json.loads(raw_data)
        # I am interested in id, created_at, screen_name, location,
        # in_reply_to_source_id, in_reply_to_screen_name, text
        print("\t".join([data['id_str'], data['created_at'], data['user'][
              'screen_name'], data['user']['location'], data['text']]))
        return True

    def on_error(self, status):
        print(status)

if __name__ == "__main__":
    # get_config()
    # api = get_twitter_api()
    # print(api.verify_credentials())
    listener = LinkListener()
    auth = get_auth()
    stream = Stream(auth, listener)
    # filtering for India
    stream.filter(locations=[70.04, 8.99, 93.0, 34.52])
