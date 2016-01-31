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

# Initialize A_freq_table
keys = list(A_text_table.keys())
for k in keys:
    aids = list(A_text_table[k].keys())
    count = 1
    for aid in aids:
        if count < 2: 
            A_freq_table[k] = {aid : 0}
        else:
            A_freq_table[k][aid] = 0
        count += 1    

entryIndex = 0
subentryIndex = 0
for aqs in answeredquestions:
    subentryIndex = 0
    for qid in aqs:
        aid = answers[entryIndex][subentryIndex]
        if aid < 0:
            continue
        A_freq_table[qid][aid] += 1
        subentryIndex += 1
    entryIndex += 1    

NQuestions = 50

qrank = 0
for k in sorted(Q_freq_table, key=Q_freq_table.get, reverse=True)[:NQuestions]:
    qrank += 1
    print('Processing question ', qrank)
    N = len(A_text_table[k])
    ind = np.arange(N)  # the x locations for the groups
    width = 1       # the width of the bars
    tally = list(A_freq_table[k].values())
    sumtally = sum(tally)
    if sumtally <= 0:
        continue
    normtally = [i*100/sumtally for i in tally]
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, normtally, width, color='r')
    # add some text for labels, title and axes ticks
    ax.set_ylabel('% of respondents')
    ax.set_title(Q_text_table[k])
    ax.set_xticks(ind + 0.5*width)
    answerText = list(A_text_table[k].values())
    ax.set_xticklabels(answerText)
    fig.savefig('Question'+str(qrank)+'.png')
    plt.close(fig)
         