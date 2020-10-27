# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:30:07 2020

@author: 10762
"""

from string import punctuation
from string import digits
from collections import Counter


def common_words(df):
  reviews = ("\n".join(i for i in df['Purpose']))
  reviews_split = ''.join([c for c in reviews.lower() if c not in punctuation]).split('\n')
  all_text = ' '.join(reviews_split)
  words = all_text.split()
  counts = Counter(words)
  vocab = sorted(counts, key=counts.get, reverse=True)
  return vocab[:10]