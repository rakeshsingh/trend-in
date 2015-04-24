# tweeter.py
import utils
from utils import UrlListener
from utils import Stream


def scrap_twitter():
    """ this function scraps twitter stream of India for URLs"""
    listener = UrlListener()
    auth = utils.get_twitter_auth()
    stream = Stream(auth, listener)
    # filtering for India
    stream.filter(locations=[70.04, 8.99, 93.0, 34.52])


def main():
    scrap_twitter()

if __name__ == "__main__":
    main()
