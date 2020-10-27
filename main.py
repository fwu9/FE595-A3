# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:05:46 2020

@author: 10762
"""

from merge_data import files
from commonest import common_words
from sentiment_analysis import best_worst

if __name__ == "__main__":
    # Read in data and merge into one data frame
    Shiraz = files('./team_data/Shiraz.txt')
    Minghao = files('./team_data/Minghao.csv')
    Fangchi = files('./team_data/Fangchi.csv')
    Yuwen = files('./team_data/Yuwen.csv')
    
    team_result = Shiraz.merge_files(Minghao, Fangchi, Yuwen)

    # Find the best and the worst business idea
    print("The best business idea comes from {0}, whose purpose is {1}.The worst business idea comes from {2}, whose purpose is {3}."
          .format(best_worst(team_result)))
    # Find the 10 most common words in the description of the companies
    print("The ten most common words are:", common_words(team_result))