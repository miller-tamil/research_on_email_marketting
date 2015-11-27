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
#python n-gram
from nltk.util import ngrams
sentence = 'this is a foo bar sentences and i want to ngramize it'
n = 6
sixgrams = ngrams(sentence.split(), n)
for grams in sixgrams:
  print grams
  
# my new reading material 
http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6006/pdf/imm6006.pdf

#emotion dictionary created from 
http://www.saifmohammad.com/Lexicons/NRC-Emotion-Lexicon-v0.92.zip

#Sentiment dataset
https://github.com/fnielsen/afinn/blob/master/afinn/data/AFINN-en-165.txt

# Our sentiment dataset is 62.5% accuratly predict the data

#Mean Sentence Length analysis
wordcounts = []
with open('re3.txt') as f:
    text = f.read()
    sentences = text.split('\n')
    for sentence in sentences:
        words = sentence.split(' ')
        wordcounts.append(len(words))
average_wordcount = sum(wordcounts)/len(wordcounts)
print("%6.2f %s" % (average_wordcount, "<== The mean sentance legnth analysis for the sample"))

#multiple csv files in to one
cat < file1.csv <(tail +2 file2.csv) <(tail +2 file3.csv) > bigfile.csv
#or
awk 'FNR > 1' file*.csv > bigfile.csv
#or
sed 1d sh*.csv > merged.csv

#word splitter
with open('words.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word) 
#spam mail collection
http://csmining.org/index.php/enron-spam-datasets.html
http://www.aueb.gr/users/ion/data/lingspam_public.tar.gz
