import okcupyd
from okcupyd.session import Session
import pickle

#from okcupyd.json_search import SearchFetchable
username = ''
password = ''

session = Session.login(username, password)
#user = okcupyd.User(session)

# Instance of question interface
question_interface = okcupyd.question.Questions(session)
# Fix importance to not important (5)
importance = 5


# Grab stuff from pickle jar
file = open('data.pkl', 'rb')

Q_freq_table=pickle.load(file)
Q_text_table=pickle.load(file)
usernames=pickle.load(file)
answeredquestions=pickle.load(file)
# Loop through question id's
for k in sorted(Q_freq_table, key=Q_freq_table.get, reverse=True)[:1000]:
    question_interface.respond(k,1,1,importance)
