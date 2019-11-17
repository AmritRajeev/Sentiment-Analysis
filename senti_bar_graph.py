from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import spacy as sp
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import nltk
import collections
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
nltk.download('punkt')
nltk.download('vader_lexicon')
from nltk.tokenize import word_tokenize, RegexpTokenizer



def get_word_sentiment(text):
    
    tokenized_text = nltk.word_tokenize(text)
    sent_obj = SentimentIntensityAnalyzer() 
 
    for word in tokenized_text:
        sentiment_dict = sent_obj.polarity_scores(word)
        if (sentiment_dict['compound']) >= 0.5:
            if(len(word)>4):
                pos_word_list.append(word)
        elif (sentiment_dict['compound']) <= 0.1:
            if(len(word)>4):
                neg_word_list.append(word)
        else:
            if(len(word)>4):
                neu_word_list.append(word)
    

# Driver code 
if __name__ == "__main__" :

    ct=0
    df=pd.read_csv(r"C:\Users\User\Desktop\python prgs\Tweets.csv")
    for i in range(0,500): 
                sentence=df.text[i]
                #df.airline_sentiment[i]=sentiment_scores(sentence)
                #print(sentiment_scores(sentence),df.text[i])
                #print(sentiment_scores(sentence),df.airline_sentiment[i])
                if(sentiment_scores(sentence)==df.airline_sentiment[i]):
                    ct+=1
                   
    
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[] 
    for i in range(0,500): 
                text=df.text[i]
                get_word_sentiment(text)
    ctrpos=collections.Counter(pos_word_list)
    #print(ctrpos)
    
    #print('Positive:',pos_word_list) 
    
    plt.bar(range(len(ctrpos)),list(ctrpos.values()),align='center')
    plt.xticks(range(len(ctrpos)),list(ctrpos.keys()))
    plt.show()
    ctrneg=collections.Counter(neg_word_list)
    #print(ctrneg)
    
    #print('Negative:',neg_word_list)     
    plt.bar(range(len(ctrneg)),list(ctrneg.values()),align='center')
    plt.xticks(range(len(ctrneg)),list(ctrneg.keys()))
    plt.show()
    
    ctrneu=collections.Counter(neu_word_list)
    #print(ctrneu)
    #print('Neutral:',neu_word_list) 
    plt.bar(range(len(ctrneu)),list(ctrneu.values()),align='center')
    plt.xticks(range(len(ctrneu)),list(ctrneu.keys()))
    plt.show()
