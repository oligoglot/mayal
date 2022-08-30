import nltk
import re
from nltk.corpus import PlaintextCorpusReader
import pandas as pd
from pandas.plotting import table 
import matplotlib.pyplot as plt

root = ".\corpora\\"
files = PlaintextCorpusReader(root, ".*")
#raw = files.raw("pathittrupathu.txt")
sents = []
# punct = {'.', '[', "'", ']', ',', ')', '\ufeff', ':', '-', '!', ';', '*', '='}
punct = re.compile("[\'\]\-\:\[\,!\.\=\*\);]")
dropper = re.compile("[\d\(]")
with open(root + "pathittrupathu.txt", encoding="utf8") as input:
    for sent in input.readlines():
        sent = re.sub(dropper, "", sent)
        sent = re.sub("\s+", " ", re.sub(punct, " ", sent)).replace("஡஢", "ரி")
        #if sent != '' and re.findall("\d", sent) == []:
        if sent.count(" ") > 2: # at least two cheers
            sents.append(sent)

pulli = '\u0BCD'
con = ['க','ங','ச','ஞ','ட', 'ண','த','ந','ப','ம','ய','ர','வ','ல', 'ள','ழ','ற','ன']
cons = ['க்', 'ங்', 'ச்' , 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'வ்', 'ல்', 'ள்', 'ழ்', 'ற்','ன்']
#for con1 in con:
#    for con2 in con:
#        for sent in sents:
#            gem = con1 + pulli + con2
#            for word in sent.split():
#                #print(gem)
#                if gem in word:
#                    print(word)
cfd = nltk.ConditionalFreqDist((con1, con2)
for con1 in con
for con2 in con
for sent in sents
for word in sent.split()
if con1 + pulli + con2 in word)
# cfd.tabulate()
#cfd.plot()
print()
nilai = cfd.keys()
varu = cfd.keys()

frame = pd.DataFrame(0, index=nilai, columns=varu)

'''
for i, c1 in enumerate(nilai):
    for j, c2 in enumerate(varu):
        print(c1)
        frame[i][j] = cfd.get(c1)
'''
for c1, v in cfd.items():
    for c2 in v.keys():
        frame[c2][c1] = v[c2]

print(frame)
ax = plt.subplot(111, frame_on=False) 
ax.xaxis.set_visible(False) 
ax.yaxis.set_visible(False) 
table(ax, frame, loc='center')  

plt.savefig('pathittrupathu.png')
'''
with open("out.csv", "w", encoding="utf8") as outf:
    cfilter = set()
    for sent in sents:
        for word in sent.split():
            for c in word:
                if ord(c) < ord('\u0B80') or ord(c) > ord('\u0BFF'):
                    #print(ord(c), c, ord(word[0]), word, sep="\t", file=outf)
                    cfilter.add(c)
    for c in cfilter:
        print(c, end="")
'''

#print(ord('\u0B80'), ord('\u0BFF'))