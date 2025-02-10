import tweepy
import schedule
import time

# Replace with your own credentials
consumer_key = '****odmyl7'
consumer_secret = '****odmyl7'
access_token = '1732241018345627648-cP3R36aeV8HzOZK10h7mkdLzGDuUfK'
access_token_secret = 'HDpas2JWTOBgaiQu7JxtQ1FKjR7gBbheOeeJaySyod017'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def post_tweet(content):
    api.update_status(status=content)
    print("Tweet posted successfully!")

def job():
    content = "Your scheduled tweet content"
    post_tweet(content)

# Schedule the tweet
schedule.every().day.at("10:00").do(job)  # Schedule for 10:00 AM every day

while True:
    schedule.run_pending()
    time.sleep(1)
