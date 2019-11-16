from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy as sp
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib as plt
import pandas as pd

def sentiment_scores(sentence):  
    sent_obj = SentimentIntensityAnalyzer() 
 
    sentiment_dict = sent_obj.polarity_scores(sentence) 
   
    if sentiment_dict['compound'] >= 0.05 : 
        return "positive"
        
    elif sentiment_dict['compound'] <= - 0.05 : 
        return "negative"
  
    else : 
        return "neutral"

def acc_check(ct):
    acc=ct/len(range(0,17))
    acc_per=acc*100
    return acc_per
    
    


# Driver code 
if __name__ == "__main__" :

    ct=0
    df=pd.read_csv(r"C:\Users\User\Desktop\python prgs\Tweets.csv")
    for i in range(0,17): 
                sentence=df.text[i]
                #df.airline_sentiment[i]=sentiment_scores(sentence)
                #print(sentiment_scores(sentence),df.text[i])
                #print(sentiment_scores(sentence),df.airline_sentiment[i])
                if(sentiment_scores(sentence)==df.airline_sentiment[i]):
                    ct+=1
                   
    acc_check(ct)
    print("The accuracy of the model is",acc_check(ct))
