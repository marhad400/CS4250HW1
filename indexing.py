#-------------------------------------------------------------------------
# AUTHOR: Mark Haddad
# FILENAME: indexing.py
# SPECIFICATION: Calculates and creates document-term matrix of collection.csv
# FOR: CS 4250- Assignment #1
# TIME SPENT: 2 hr 30 min
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0])


#Conducting stopword removal. Hint: use a set to define your stopwords.
#--> add your Python code here
stopWords = {"I", "and", "She", "she", "Her", "her", "They", "they", "Their", "their"}

#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
#--> add your Python code here
stemming = {
    "love": ["loves", "loved", "loving"],
    "cat": ["cats"],
    "dog": ["dogs"]
    }

#Identifying the index terms.
#--> add your Python code here
terms = list(stemming.keys())


#Building the document-term matrix by using the tf-idf weights.
#--> add your Python code here
document_count = len(documents)
docTermMatrix = [[0 for _ in terms] for _ in range(document_count)]

term_frequency = [dict.fromkeys(stemming, 0) for _ in range(document_count)]

for index, document in enumerate(documents):
    for word in document.split(" "):
        word = word.lower()
        for key, stems in stemming.items():
            if word == key or word in stems:
                term_frequency[index][key] += 1

for document in term_frequency:
    valid_total = 0
    for key, value in document.items():
      valid_total += value
    for key in document:
        document[key] /= valid_total
    

document_frequency = dict.fromkeys(stemming, 0)
for document in term_frequency:
    for key, value in document.items():
        if value > 0:
            document_frequency[key] += 1


for master_term, doc_freq in document_frequency.items():
    inner = document_count / doc_freq
    idf = math.log(inner, 10)
    for doc_index, document in enumerate(term_frequency):
        for term_index, (term, term_freq) in enumerate(document.items()):
            if term == master_term:
                docTermMatrix[doc_index][term_index] = idf * term_freq

#Printing the document-term matrix.
#--> add your Python code here
[print("\t\t".join(list(map(str, i)))) for i in docTermMatrix]