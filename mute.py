import twitter

CONSUMER_KEY = 'WWWWWWWW'
CONSUMER_SECRET = 'XXXXXXXX'
ACCESS_TOKEN = 'YYYYYYYY'
ACCESS_TOKEN_SECRET = 'ZZZZZZZZ'


# Create an Api instance.
api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN,
                  access_token_secret=ACCESS_TOKEN_SECRET)

ids = api.GetFriendIDs()

for id in ids:
    api.CreateMute(user_id=id)