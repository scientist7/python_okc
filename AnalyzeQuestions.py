import pickle
import numpy as np
import matplotlib.pyplot as plt

# Grab stuff from pickle jar
file = open('AllData.pkl', 'rb')

Q_freq_table=pickle.load(file)
Q_text_table=pickle.load(file)
A_text_table=pickle.load(file)
usernames=pickle.load(file)
answeredquestions=pickle.load(file)
myanswermatches=pickle.load(file)
answers=pickle.load(file)

file.close()

A_freq_table = {}

entryIndex = 0
subentryIndex = 0
for aqs in answeredquestions:
    for qid in aqs:
    

NQuestions = 1

for k in sorted(Q_freq_table, key=Q_freq_table.get, reverse=True)[:NQuestions]:
    N = len(A_text_table[k])
         