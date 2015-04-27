# basic utilities
import json
import tweepy
import csv
import time

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


def get_config():
    """ read configuration and load into a json object """
    try:
        with open('config.json') as config_file:
            config = json.load(config_file)
            return config
    except IOError as err:
        print("OS error: {0}".format(err))

    return True


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
        datafile = '/tmp/' + 'data_' + time.strftime("%Y-%m-%d") + ".tsv"
        data = json.loads(status)
        # get attributes and do cleanup
        tweet_text = data['text']
        tweet_screen_name = data['user']['screen_name']
        tweet_location = data['user']['location']
        tweet_text = tweet_text.strip(' \t\n\r')
        tweet_screen_name = tweet_screen_name.strip(' \t\n\r')
        tweet_location = tweet_location.strip(' \t\n\r')

        # I am interested in id, created_at, screen_name, location,
        # in_reply_to_source_id, in_reply_to_screen_name, text

        with open(datafile, 'a', encoding='utf8') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter='\t', quotechar='|')
            csvwriter.writerow(
                [data['id_str'], data['created_at'], tweet_screen_name, tweet_location, tweet_text])
            # csvwriter.write('\n')
        return True

    def on_error(self, status):
        print("below status code was returned")
        print(status)

    def on_exception(self, exception):
        """
        handle exception
        """
        raise exception
        return False
