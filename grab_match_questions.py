import okcupyd
import hashlib
from okcupyd.session import Session
import numpy.random
import time
import pickle

# Read in known profiles to skip
path = "C:\\Users\\Ben\\Desktop\\okcstuff\\python\\"
readprof = open(path+'unames.pkl','rb')
markedunames = pickle.load(readprof)
readprof.close()


#from okcupyd.json_search import SearchFetchable
username = 'PoggyBiggles'
password = 'Junart12!'

session = Session.login(username, password)
user = okcupyd.User(session)

# Get match profiles
profiles = user.search(age_min=25, age_max=41)


output = open('data.pkl', 'wb')

# Lists for profile info
usernames = []
userids = []
answeredquestions = []
myanswermatches = []
answers = []
# Hash tables for questions
Q_freq_table = {}
Q_text_table = {}
A_text_table = {}
pcounter = 0
nCollect = 250

# Parameters for time delay in scraping
mean = 1
sigma = 1

# Make hash table of answer id and text
for q in user.questions.not_important:
    uq=user.get_user_question(q)
    qid = uq.id
    for options in uq.answer_options:
        aid = options.id
        answer_text = options.text
        if qid in A_text_table:
            A_text_table[qid][aid] = answer_text    
        else:
            A_text_table[qid] = {aid : answer_text}

# Function to make hash table of answer id's
def InsertAnswer(qid,answer_text,answerlist):
    if answer_text == '':
        answerlist.append(-1)
    if qid in A_text_table:
        if answer_text in A_text_table[qid].values():
            aid = list(A_text_table[qid].keys())[list(A_text_table[qid].values()).index(answer_text)]
            answerlist.append(aid)
        else:
            answerlist.append(-2)    
    else:
        answerlist.append(-3)
                    
# Loop through profiles
for p in profiles:
    if p.username in markedunames:
        continue
    pcounter +=1
    print (pcounter)
    
    usernames.append(p.username)
    userids.append(p._current_user_id)
    profile_answered_questions = []
    profile_answer_match = []
    answerlist = []    
    # Loop through answered questions
    for q in p.questions:
        profile_answered_questions.append(q.id)
        profile_answer_match.append(q.my_answer_matches)
        InsertAnswer(q.id,q.their_answer,answerlist)
        if q.id in Q_freq_table:
            Q_freq_table[q.id]+=1
        
        else:
            Q_text_table[q.id]=q.text
            Q_freq_table[q.id]=0
    answeredquestions.append(profile_answered_questions)
    myanswermatches.append(profile_answer_match)
    answers.append(answerlist)    
    if pcounter >= nCollect:
        break
    #Random delay between profile scraping
    time.sleep(min(abs(numpy.random.normal(mean,sigma)),5))

            
pickle.dump(Q_freq_table,output)
pickle.dump(Q_text_table,output)
pickle.dump(usernames,output)
pickle.dump(userids,output)
pickle.dump(answeredquestions,output)
pickle.dump(myanswermatches,output)
pickle.dump(answers,output)
pickle.dump(A_text_table,output)
output.close()            