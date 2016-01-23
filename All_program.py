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

# empty line remove
sed '/^\s*$/d'

#emotion ref
chrome-extension://ecnphlgnajanjnkcmbpancdjoidceilk/http://arxiv.org/pdf/1205.4944.pdf

#intensions ref
https://repositories.lib.utexas.edu/handle/2152/18054

#best ref
http://content.adestra.com/hubfs/2015_Reports_and_eGuides/2015_Subject_Line_Report.pdf
# mmain ref
http://www.academypublisher.com/jetwi/vol01/no1/jetwi01016076.pdf
#to draw a paser tree in regersive 
from textblob import TextBlob
wiki = TextBlob(open('full.txt','rU').read())
a=wiki.tags
import nltk 
sentence = a

pattern = """NP: {<DT>?<JJ>*<NN>}
VBD: {<VBD>}
IN: {<IN>}"""
NPChunker = nltk.RegexpParser(pattern) 
result = NPChunker.parse(sentence)
result.draw()

# regresive array input for pos taging 
from pattern.en import parse
from pattern.en import pprint 

with open('spam.txt', 'rU') as ins:
    array = []
    for line in ins:
        array.append(line)
for i in array:
	pprint(parse(i, relations=True, lemmata=True))
