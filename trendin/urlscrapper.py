# tweeter.py
import time
import utils
from utils import UrlListener
from tweepy import Stream


def scrap_twitter():
    """ this function scraps twitter stream of India for URLs"""
    listener = UrlListener()
    auth = utils.get_twitter_auth()
    tweetstream = Stream(auth, listener)
    while True:
        # right before midnight close the  stream so that next run can take
        # another files
        if time.localtime().tm_hour == 23:
            if tweetstream.running is True:
                tweetstream.disconnect()
        else:
            if tweetstream.running is False:
                # filtering for India
                tweetstream.filter(
                    locations=[70.04, 8.99, 93.0, 34.52], async=True)
        # wake up every 10 minutes to check the stream status
        time.sleep(600)


def main():
    scrap_twitter()

if __name__ == "__main__":
    main()
