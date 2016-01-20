import pickle
import os

# Get all data files to combine
path = "C:\\Users\\Ben\\Desktop\\okcstuff\\python"
dirs = os.listdir( path )

datafiles = []
totalusernames = []
totaluserids = []


datafilecounter = 0
for file in dirs:
    if "data" not in file:
        continue
    # Open data file
    datadump = open(file,'rb')  
    datafilecounter = datafilecounter + 1
    # load objects from the file 
    Q_freq_table_dump = pickle.load(datadump)
    Q_text_table_dump = pickle.load(datadump)
    usernames_dump = pickle.load(datadump)
    userids_dump = pickle.load(datadump)
    
    if datafilecounter==1:
        totalusernames = usernames_dump
        totaluserids = userids_dump
    
    else:
        for uname in usernames_dump:
            if uname not in totalusernames:
                totalusernames.append(uname)
    datadump.close()            
output = open('unames.pkl', 'wb')  
print (len(totalusernames))              
pickle.dump(totalusernames,output)
output.close()