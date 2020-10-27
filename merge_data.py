# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 18:27:00 2020

@author: 10762
"""

import pandas as pd
import numpy as np

class files():

  def __init__(self, name):
    ''' name is the document name, including".csv" or ".txt" '''
    ''' csv's type = 1, else = 0 '''

    self.name = name
    self.type = self.name[-4:] == ".csv"

  def read_doc(self):
    Name = []
    Purpose = []
    if self.type == 1:
      result = pd.read_csv(self.name)
      if 'Name' in result['Name'][0]:
        Name = [name[6:] for name in result['Name']]
      if 'Purpose' in result['Purpose'][0]:
        Purpose = [purpose[9:] for purpose in result['Purpose']]
        result = pd.DataFrame({'Name': Name, 'Purpose': Purpose})
    
    if self.type == 0:
      doc = open(self.name, 'r')
      result = doc.readlines()
      Name = [result[0].strip("['").strip("']").split("', '")[i] for i in range(100) if i%2==0]
      Purpose = [result[0].strip("['").strip("']").split("', '")[i] for i in range(100) if i%2==1]
      result = pd.DataFrame({'Name': Name, 'Purpose': Purpose})
    
    return result

  def merge_files(self, other1, other2, other3):

    return self.read_doc().append(other1.read_doc()).append(other2.read_doc()).append(other3.read_doc())