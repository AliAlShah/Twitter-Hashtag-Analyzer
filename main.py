from tweet_retriever import *
from twitter_sentiment_model import *
from plots import *

from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)

#Getting tweets
tweets = get_tweets(input("What keyword are you interested in???    \n"), int(input("How many tweets do you want to collect\n")))
positive_sentiment_count = 0
neutral_sentiment_count = 0
negative_sentiment_count = 0


#Converting @username to @user and converting all links to just http, this is so roberta is most effective
processed_tweets_list = []
tweet_words = []
for tweet in tweets:
    for word in tweet.split(' '):
        if word.startswith('@') and len(word) > 1:
            word = '@user'
        elif word.startswith('http'):
            word= 'http'
        tweet_words.append(word)
    processed_tweets_list.append(" ".join(tweet_words))
    tweet_words = []


#passing each tweet into model and keeping count of sentiments
for tweet in processed_tweets_list:
    prediction = predict(tweet)
    if prediction == 1:
        positive_sentiment_count += 1
    elif prediction == 0:
        neutral_sentiment_count += 1
    else:
        negative_sentiment_count += 1
print(f"POSITIVE SENTIMENT COUNT: {positive_sentiment_count}\n")
print(f"NEGATIVE SENTIMENT COUNT: {negative_sentiment_count}\n")
print(f"NEUTRAL SENTIMENT COUNT: {neutral_sentiment_count}\n")

#Plotting bar chart and pie chart
plot(posititve=positive_sentiment_count, negative=negative_sentiment_count, neutral=neutral_sentiment_count)
pieplot(posititve=positive_sentiment_count, negative=negative_sentiment_count, neutral=neutral_sentiment_count)