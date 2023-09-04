import nltk
import re
from nltk.corpus import PlaintextCorpusReader
import pandas as pd
import dataframe_image as dfi

root = ".\\corpora\\"
files = PlaintextCorpusReader(root, ".*")

#raw = files.raw("பதிற்றுப்பத்து.txt")

# punct = {'.', '[', "'", ']', ',', ')', '\ufeff', ':', '-', '!', ';', '*', '='}
punct = re.compile("[\'\]\-\:\[\,!\.\=\*\);]")
dropper = re.compile("[\d\(]")
pulli = '\u0BCD'
con = ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'ற', 'ன', 'த', 'ந', 'ப', 'ம', 'ய', 'வ', 'ர', 'ல', 'ள', 'ழ']
cons = ['க்', 'ங்', 'ச்' , 'ஞ்', 'ட்', 'ண்', 'ற்', 'ன்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'வ்', 'ர்', 'ல்', 'ள்', 'ழ்']
iso = {'': '∅', 'க' : 'k', 'ங': 'ṅ', 'ச': 'c', 'ஞ': 'ñ', 'ட': 'ṭ', 'ண': 'ṇ', 'ற': 'ṟ', 'ன': 'ṉ', 'த': 't', 'ந': 'n', 'ப': 'p', 'ம': 'm', 'ய': 'y', 'வ': 'v', 'ர': 'r', 'ல': 'l', 'ள': 'ḷ', 'ழ': 'ḻ'}
iso_cons = ['∅', 'k', 'ṅ', 'c' , 'ñ', 'ṭ', 'ṇ', 'ṟ', 'ṉ', 't', 'n', 'p', 'm', 'y', 'v', 'r', 'l', 'ḷ', 'ḻ']

class MayalProcessor:
    def max_likelihood(self, s: pd.Series):
        '''
        Maximum Likelihood Estimation: P(c2|c1)= count(c1,c2)/count(c1)
        '''
        return s/s.sum()

    def highlight_max_both_axes(self, s: pd.DataFrame):
        '''
        Assign a background colour showing rowwise and columnwise maxes.
        '''
        ret = pd.DataFrame(0, index=self.nilai, columns=self.varu)
        rmax = s.max(axis=1)
        cmax = s.max()
        for i, n in enumerate(self.nilai):
            for j, v in enumerate(self.varu):
                if s[v][n] == rmax[n] and s[v][n] == cmax[v]:
                    color = "teal"
                elif s[v][n] == rmax[n]:
                    color = "pink"
                elif s[v][n] == cmax[v] and s[v][n] > 0:
                    color = "yellow"
                else:
                    color = "white"
                ret.iloc[i, j] = "background-color: %s" % color
        return ret

    def process(self, work):
        def get_css(s: pd.Series):
            '''
            pick css value for a series
            '''
            ret = [css.loc[i, s.name] for i in s.index]
            return ret

        print("Processing " + work)
        sents = self.preprocess_work(work)
        cfd = nltk.ConditionalFreqDist(self.compute_cfd(sents))

        self.nilai = iso_cons
        self.varu = iso_cons

        frame = pd.DataFrame(0, index=self.nilai, columns=self.varu)

        for c1, v in cfd.items():
            for c2 in v.keys():
                frame[c2][c1] = v[c2]


        css = self.highlight_max_both_axes(frame)

        dfi.export(frame.style.set_properties(**{'border': '1.3px solid black', 'color': 'black', 'padding': '5px'}).apply(get_css), "out\\" + work + ".png", dpi=300)

        pd.set_option("styler.format.precision", 3)
        row_mle = frame.apply(self.max_likelihood, axis = 1)
        css = self.highlight_max_both_axes(row_mle)
        row_mle.fillna('-', inplace=True)

        dfi.export(row_mle.style.set_properties(**{'border': '1.3px solid black', 'color': 'black', 'padding': '5px'}).apply(get_css), "out\\" + work + "_row_mle.png", dpi=300)

        col_mle = frame.apply(self.max_likelihood, axis = 0)
        css = self.highlight_max_both_axes(col_mle)
        col_mle.fillna('-', inplace=True)

        dfi.export(col_mle.style.set_properties(**{'border': '1.3px solid black', 'color': 'black', 'padding': '5px'}).apply(get_css), "out\\" + work + "_col_mle.png", dpi=300)

    def preprocess_work(self, work):
        sents = []
        text = root + work + ".txt"
        with open(text, encoding="utf8") as input:
            for sent in input.readlines():
                sent = re.sub(dropper, "", sent)
                sent = re.sub("\s+", " ", re.sub(punct, " ", sent)).replace("஡஢", "ரி")
                if sent.count(" ") > 2: # at least two cheers
                    sents.append(sent)
        return sents

    def compute_cfd(self, sents):
        ret = []  
        for sent in sents:
            for word in sent.split():
                for con1 in con:
                    if word.startswith(con1):
                        ret.append((iso[''], iso[con1]))
                    if word.endswith(con1):
                        ret.append((iso[con1], iso['']))
                    for con2 in con:
                        if con1 + pulli + con2 in word:
                            ret.append((iso[con1], iso[con2]))
                        
        return ret

p = MayalProcessor()
works = ["ainkurunuru", "akananuru", "kalithokai", "kurunthokai", "natrinai", "paripadal", "pathittrupathu", "purananuru", "எட்டுத்தொகை-consolidated"]
for work in works:
    p.process(work)