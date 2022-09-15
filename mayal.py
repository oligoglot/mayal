import nltk
import re
from nltk.corpus import PlaintextCorpusReader
import pandas as pd
import dataframe_image as dfi

def highlight_max_both_axes(s: pd.DataFrame):
    '''
    Assign a background colour showing rowwise and columnwise maxes.
    '''
    ret = pd.DataFrame(0, index=nilai, columns=varu)
    rmax = s.max(axis=1)
    cmax = s.max()
    for i, n in enumerate(nilai):
        for j, v in enumerate(varu):
            if s[v][n] == rmax[n] and s[v][n] == cmax[v]:
                color = "blue"
            elif s[v][n] == rmax[n]:
                color = "red"
            elif s[v][n] == cmax[v] and s[v][n] > 0:
                color = "yellow"
            else:
                color = "white"
            ret.iloc[i, j] = "background-color: %s" % color
    return ret

def get_css(s: pd.Series):
    '''
    pick css value for a series
    '''
    ret = [css.loc[i, s.name] for i in s.index]
    return ret

root = ".\\corpora\\"
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
        if sent.count(" ") > 2: # at least two cheers
            sents.append(sent)

pulli = '\u0BCD'
con = ['க','ங','ச','ஞ','ட', 'ண','ற','ன','த','ந','ப','ம','ய','ர','வ','ல', 'ள','ழ']
cons = ['க்', 'ங்', 'ச்' , 'ஞ்', 'ட்', 'ண்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'ர்', 'வ்', 'ல்', 'ள்', 'ழ்', 'ற்','ன்']

cfd = nltk.ConditionalFreqDist((con1, con2)
for con1 in con
for con2 in con
for sent in sents
for word in sent.split()
if con1 + pulli + con2 in word)

nilai = cfd.keys()
varu = cfd.keys()

frame = pd.DataFrame(0, index=nilai, columns=varu)

for c1, v in cfd.items():
    for c2 in v.keys():
        frame[c2][c1] = v[c2]


css = highlight_max_both_axes(frame)

dfi.export(frame.style.set_properties(**{'border': '1.3px solid black', 'color': 'black'}).apply(get_css), "pathittrupathu.png")