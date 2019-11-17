from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy as sp
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib as plt
import pandas as pd
import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize, RegexpTokenizer


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

def get_word_sentiment(text):
    
    tokenized_text = nltk.word_tokenize(text)
    sent_obj = SentimentIntensityAnalyzer() 
 
    for word in tokenized_text:
        sentiment_dict = sent_obj.polarity_scores(word)
        if (sentiment_dict['compound']) >= 0.1:
            pos_word_list.append(word)
        elif (sentiment_dict['compound']) <= -0.1:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)
    

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
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[] 
    for i in range(0,17): 
                text=df.text[i]
                get_word_sentiment(text)
    
    print('Positive:',pos_word_list)        
    print('Negative:',neg_word_list) 
    for j in neu_word_list:
        if (len(j)<=4):
            neu_word_list.remove(j)
    neu_word_list.remove('@')        
    print('Neutral:',neu_word_list)
