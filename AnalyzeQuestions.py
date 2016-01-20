import pickle


# Grab stuff from pickle jar
file = open('data.pkl', 'rb')

Q_freq_table=pickle.load(file)
Q_text_table=pickle.load(file)
usernames=pickle.load(file)
answeredquestions=pickle.load(file)

for k in sorted(Q_freq_table, key=Q_freq_table.get, reverse=True)[:30]:
    print Q_text_table[k], Q_freq_table[k]
         