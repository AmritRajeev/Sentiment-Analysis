from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy as sp
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib as plt
import pandas as pd

def sentiment_scores(sentence,sentiment):  
    sent_obj = SentimentIntensityAnalyzer() 
 
    sentiment_dict = sent_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
   
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive")
        return 1
        
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative")
        return 0
  
    else : 
        print("Neutral")


        
# Driver code 
if __name__ == "__main__" :

    sentence = ""
    sentiment_scores(sentence)
