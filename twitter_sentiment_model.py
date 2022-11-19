from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

#Loading roberta twitter sentiment analysis model
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
labels = ['Negative', 'Neutral', 'Positive']


#Creating function to predict sentiment of an individual tweet
def predict(tweet):
    #Encoding tweet before passing it through the model
    encoded_tweet = tokenizer(tweet, return_tensors='pt')
    #Storing result of model
    output = model(**encoded_tweet)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores = list(scores)
    print(scores)

    #Checking sentiment of model
    if scores.index(max(scores)) == 0:
        print(f"TWEET: {tweet} is a NEGATIVE SENTIMENT")
        return -1
    elif scores.index(max(scores)) == 1:
        print(f"TWEET: {tweet} is a NEUTRAL SENTIMENT")
        return 0
    elif scores.index(max(scores)) == 2:
        print(f"TWEET: {tweet} is a POSITIVE SENTIMENT")
        return 1

