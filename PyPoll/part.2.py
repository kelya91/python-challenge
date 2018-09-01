
# coding: utf-8

# In[28]:


# Dependencies
import csv
import os

file_to_load = "election_data.csv"
file_to_output = "election_analysis_.txt"
csvpath = os.path.join('..','Resources','election_data.csv')
with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


# In[29]:


totalVotes = 0
CandidatesList =[]
voterCount ={}
winervotes = 0
winerCand =''


# In[67]:


with open (file_to_load) as election_data:
    reader = csv.reader(election_data)
    next (election_data)
    for row in reader:
        totalVotes= totalVotes+1
        candidate =row[2]
        if candidate not in CandidatesList:
            CandidatesList.append(candidate)
            voterCount[candidate]= 0
        voterCount[candidate]= voterCount[candidate]+1
      
        


# In[72]:


winervotes = 0
winerCand =''
for candidate in voterCount:
            Candvotes = voterCount[candidate]
           

            
            if Candvotes > winervotes:
                    winerCand = candidate
                    winervotes = Candvotes

                    


# In[76]:


election_results= (
f"\n\nElection Results\n"
f"---------------------\n"
f" Total votes: {totalVotes}\n"
f" The candidate's votes :{voterCount}\n"

f" The Winning candidate:{winerCand}\n"
f" Wining% :{round(winervotes/totalVotes*100,1)}\n")
print(election_results)

with open(file_to_output, "w") as txt_file:
    txt_file.write(election_results)

