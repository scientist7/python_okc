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

# Function to make hash table of answer id's
def FillAnswer(qid,aid):
    if qid in A_freq_table:
        if aid in A_freq_table[qid]:
            A_freq_table[qid][aid] += 1
            
        else:
            A_freq_table[qid][aid] = 0  
    else:
        A_freq_table[qid] = {aid : 0}


entryIndex = 0
subentryIndex = 0
for aqs in answeredquestions:
    subentryIndex = 0
    for qid in aqs:
        aid = answers[entryIndex][subentryIndex]
        FillAnswer(qid,aid)
        subentryIndex += 1
    entryIndex += 1    

NQuestions = 1

for k in sorted(Q_freq_table, key=Q_freq_table.get, reverse=True)[:NQuestions]:
    N = len(A_text_table[k])
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, A_freq_table[k], width, color='r')
    plt.show()
         