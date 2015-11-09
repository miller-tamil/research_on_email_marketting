#This file contain and will update with all the programs i used ...
#Empty line remover
sed -e '/^[[:blank:]]*$/d' source_file > newfile

#Frequency word count.
files = list_of_files
fd = nltk.FreqDist()
for file in files:
    with open(file) as f:
        for sent in nltk.sent_tokenize(f.lower()):
            for word in nltk.word_tokenize(sent):
                fd.inc(word)

