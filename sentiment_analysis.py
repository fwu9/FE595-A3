# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:41:44 2020

@author: 10762
"""
from snownlp import SnowNLP

def best_worst(df):

  sentiment_list = [SnowNLP(purpose).sentiments for purpose in df['Purpose']]
  df['Sentiment_value'] = sentiment_list
  sentiment_ascending = df.sort_values('Sentiment_value', ascending=False)
  sentiment_ascending.reset_index(drop=True, inplace=True)
  result = (sentiment_ascending['Name'][0], sentiment_ascending['Purpose'][0],
            sentiment_ascending['Name'][199], sentiment_ascending['Purpose'][199])
  return result