import nltk
import re
from nltk.corpus import PlaintextCorpusReader
import pandas as pd
import dataframe_image as dfi

def highlight_max_both_axes(s):
    pass

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
con = ['க','ங','ச','ஞ','ட', 'ண','ற','ன','த','ந','ப','ம','ய','ர','வ','ல', 'ள','ழ']
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
# save_df_as_image(frame, "pathittrupathu.png")
dfi.export(frame.style.highlight_max(axis=1, color='blue'), "pathittrupathu.png")
# frame.style.apply(highlight_max_both_axes)