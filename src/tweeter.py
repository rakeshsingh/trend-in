# tweeter.py
import myutils

api = myutils.get_twitter_api()
for status in (api.GetUserTimeline(screen_name='sagarikaghose')):
    print(status.text.encode('utf-8'))
