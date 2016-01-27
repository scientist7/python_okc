import pickle
import os

# Get all data files to combine
path = "C:\\Users\\Ben\\Desktop\\okcstuff\\python"
dirs = os.listdir( path )

datafiles = []
totalusernames = []
totalansweredquestions = []
totalmyanswermatches = []
totalanswers = []
totalQFreqTable = {}
totalQTextTable = {}
totalATextTable = {}
index = 0


datafilecounter = 0
for file in dirs:
    if "data" not in file:
        continue
    # Open data file
    datadump = open(file,'rb')  
    datafilecounter +=  1
    # load objects from the file 
    Q_freq_table_dump = pickle.load(datadump)
    Q_text_table_dump = pickle.load(datadump)
    usernames_dump = pickle.load(datadump)
    userids_dump = pickle.load(datadump)
    aquestions_dump = pickle.load(datadump)
    myanswermatches_dump = pickle.load(datadump)
    answers_dump = pickle.load(datadump)
    A_text_table_dump = pickle.load(datadump)
    
    if datafilecounter==1:
        totalusernames = usernames_dump
        totalansweredquestions = aquestions_dump
        totalmyanswermatches = myanswermatches_dump
        totalanswers = answers_dump
        totalQFreqTable = Q_freq_table_dump
        totalQTextTable = Q_text_table_dump
        totalATextTable = A_text_table_dump
    
    else:
        index = 0
        for uname in usernames_dump:
            if uname not in totalusernames:
                totalusernames.append(uname)
                totalansweredquestions.append(aquestions_dump[index])
                totalmyanswermatches.append(myanswermatches_dump[index])
                totalanswers.append(answers_dump[index])
                # Loop through user's questions
                for aq in aquestions_dump[index]:
                    if aq in totalQFreqTable:
                        totalQFreqTable[aq] += 1
                    else:
                        totalQFreqTable[aq] = 0
                        totalQTextTable[aq] = Q_text_table_dump[aq]
            index += 1    
    datadump.close()
# Special file with usernames            
output = open('unames.pkl', 'wb')  
print (len(totalusernames))              
pickle.dump(totalusernames,output)
output.close()
# Combined file of everything
output = open('AllData.pkl','wb')
pickle.dump(totalQFreqTable,output)
pickle.dump(totalQTextTable,output)
pickle.dump(totalATextTable,output)
pickle.dump(totalusernames,output)
pickle.dump(totalansweredquestions,output)
pickle.dump(totalmyanswermatches,output)
pickle.dump(totalanswers,output)
output.close()