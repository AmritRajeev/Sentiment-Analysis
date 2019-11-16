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


        
# Driver code 
if __name__ == "__main__" :

    df=pd.read_csv(r"C:\Users\User\Desktop\python prgs\Tweets.csv")
    for i in range(1,11): 
                sentence=df.text[i]
                sentiment_scores(sentence)
