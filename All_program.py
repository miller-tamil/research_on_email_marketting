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

