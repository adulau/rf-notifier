import configparser
from mastodon import Mastodon

config = configparser.ConfigParser()
config.read('../etc/rt-notifier.config')
m = Mastodon(access_token = config['Mastodon']['access_token'], api_base_url = config['Mastodon']['api_base_url'])
m.toot("test")
