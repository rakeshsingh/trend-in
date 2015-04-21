# tweeter.py
import utils

api = utils.get_twitter_api()
print(api.get_user('rakesh'))
