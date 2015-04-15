#basic utilities 
import json
import twitter
from pprint import pprint

def get_config():
	try:
		with open('../config.json') as config_file:
			config = json.load(config_file)
			#print(config["twitter"]["consumer_key"])
			return config
	except IOError, e:
		print(e)

def get_logger():
	return None

def get_twitter_api():
	config = get_config()
	api = twitter.Api(
	consumer_key=config["twitter"]["consumer_key"],
	consumer_secret=config["twitter"]["consumer_secret"],
	access_token_key=config["twitter"]["access_token"],
	access_token_secret=config["twitter"]["access_token_secret"]
	)
	return api


if __name__ == "__main__":
	get_config()
	api = get_twitter_api()
	print(api.VerifyCredentials())
