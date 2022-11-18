from tweet_retriever import *
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

#Getting tweets
tweets = get_tweets(input("What keyword are you interested in???    \n"), int(input("How many tweets do you want to collect\n")))
positive_sentiment_count = 0
negative_sentiment_count = 0

#Loading model and dfidf vectorizer 
model = pickle.load(open("model", "rb"))
tfidf = pickle.load(open("tfidf", "rb"))

#Looping through all the tweets and passing them into machine learning model
n = 0
for tweet  in tweets:
    print(f"{n/len(tweets)}")
    n += 1
    tweet_sentiment = model.predict(tfidf.transform([tweet]))
    if tweet_sentiment == 1:
        positive_sentiment_count += 1
    else:
        negative_sentiment_count += 1
    
    print(f"TWEET: {tweet}\n TWEET SENTIMENT: {tweet_sentiment}\n")
print(f"POSITIVE SENTIMENT COUNT: {positive_sentiment_count}\n")
print(f"NEGATIVE SENTIMENT COUNT: {negative_sentiment_count}\n")
print(f"POSITIVE SENTIMENT PERCENTAGE: {positive_sentiment_count/(positive_sentiment_count + negative_sentiment_count)}\n")
print(f"NEGATIVE SENTIMENT PERCENTAGE: {negative_sentiment_count/(positive_sentiment_count + negative_sentiment_count)}\n")