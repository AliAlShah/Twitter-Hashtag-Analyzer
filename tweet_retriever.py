from hidden_details import Details
import tweepy

#Loading API details from hidden file
api_key = Details.api_key()
api_secret_key = Details.api_key_secret()
access_token = Details.access_token()
access_secret_token = Details.access_token_secret()

#authenticating twitter API and access token
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_secret_token)
api = tweepy.API(auth)


def get_tweets(key_word, limit):
    #collecting tweets which include the keyword given in the function and limiting the number of tweets to the other argument of the function
    tweets = tweepy.Cursor(api.search_tweets, q=key_word, count=100, tweet_mode='extended', lang='en').items(limit)
    tweets_list = [tweet.full_text for tweet in tweets]
    #returning list of tweets collected
    return tweets_list
