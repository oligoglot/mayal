from typing import Counter
import nltk
import re
import pandas as pd
import dataframe_image as dfi
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt

root = "./corpora/"

# punct = {'.', '[', "'", ']', ',', ')', '\ufeff', ':', '-', '!', ';', '*', '='}
punct = re.compile("[\'\]\-\:\[\,!\.\=\*\);]")
dropper = re.compile("[\d\(]")
pulli = '\u0BCD'
con = ['க', 'ங', 'ச', 'ஞ', 'ட', 'ண', 'ற', 'ன', 'த', 'ந', 'ப', 'ம', 'ய', 'வ', 'ர', 'ல', 'ள', 'ழ']
cons = ['க்', 'ங்', 'ச்', 'ஞ்', 'ட்', 'ண்', 'ற்', 'ன்', 'த்', 'ந்', 'ப்', 'ம்', 'ய்', 'வ்', 'ர்', 'ல்', 'ள்', 'ழ்']
iso = {'க': 'k', 'ங': 'ṅ', 'ச': 'c', 'ஞ': 'ñ', 'ட': 'ṭ', 'ண': 'ṇ', 'ற': 'ṟ', 'ன': 'ṉ', 'த': 't', 'ந': 'n', 'ப': 'p',
       'ம': 'm', 'ய': 'y', 'வ': 'v', 'ர': 'r', 'ல': 'l', 'ள': 'ḷ', 'ழ': 'ḻ'}
iso_cons = ['k', 'ṅ', 'c', 'ñ', 'ṭ', 'ṇ', 'ṟ', 'ṉ', 't', 'n', 'p', 'm', 'y', 'v', 'r', 'l', 'ḷ', 'ḻ']
plosives = set(['k', 'c', 'ṭ', 'ṟ', 'p', 't'])
nasals = set(['ṅ', 'ñ', 'ṇ', 'ṉ', 'n', 'm'])


class MayalProcessor:
    def max_likelihood(self, s: pd.Series):
        '''
        Maximum Likelihood Estimation: P(c2|c1)= count(c1,c2)/count(c1)
        '''
        return s / s.sum()

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

    def process(self, imode, collection, work):
        print("Processing", imode, collection, work)
        sents = self.preprocess_work(imode, collection, work)

        for to_merge in [True, False]:
            if imode == "யாப்பு":
                if to_merge:
                    # overestimation
                    text_type = "Type2"
                else:
                    text_type = "Type1"
            else:
                if to_merge:
                    text_type = "Type4"
                else:
                    # under estimation
                    text_type = "Type3"
            freqs = self.compute_cfd(''.join(sents), to_merge)
            counts = self.phonetype_counts(freqs)
            filepathprefix = "out/" + text_type + "/" + collection + "/" + imode + "_" + "_" + work
            if to_merge:
                filepathprefix = filepathprefix + "_merged"
            self.output(filepathprefix, freqs, counts)

    def output(self, filepathprefix, freqs, counts):
        self.plot_pie(filepathprefix, counts)
        self.tabulate(filepathprefix, freqs)

    def tabulate(self, filepathprefix, freqs):
        def get_css(s: pd.Series):
            '''
            pick css value for a series
            '''
            ret = [css.loc[i, s.name] for i in s.index]
            return ret

        cfd = nltk.ConditionalFreqDist(freqs)

        self.nilai = iso_cons
        self.varu = iso_cons

        frame = pd.DataFrame(0, index=self.nilai, columns=self.varu)

        for c1, v in cfd.items():
            for c2 in v.keys():
                frame[c2][c1] = v[c2]

        frame.to_csv(filepathprefix + ".csv")
        css = self.highlight_max_both_axes(frame)
        dfi.export(
            frame.style.set_properties(**{'border': '1.3px solid black', 'color': 'black', 'padding': '5px'}).apply(
                get_css), filepathprefix + ".png", dpi=300)

        pd.set_option("styler.format.precision", 3)
        row_mle = frame.apply(self.max_likelihood, axis=1)
        css = self.highlight_max_both_axes(row_mle)
        row_mle.fillna('-', inplace=True)

        dfi.export(
            row_mle.style.set_properties(**{'border': '1.3px solid black', 'color': 'black', 'padding': '5px'}).apply(
                get_css), filepathprefix + "_row_mle.png", dpi=300)

        col_mle = frame.apply(self.max_likelihood, axis=0)
        css = self.highlight_max_both_axes(col_mle)
        col_mle.fillna('-', inplace=True)

        dfi.export(
            col_mle.style.set_properties(**{'border': '1.3px solid black', 'color': 'black', 'padding': '5px'}).apply(
                get_css), filepathprefix + "_col_mle.png", dpi=300)

    def plot_pie(self, filepathprefix, counts):
        fig = plt.figure(figsize=(5, 5))
        plt.pie(counts.values(), labels=counts.keys(), autopct='%1.0f%%')
        fig.savefig(filepathprefix + "-pie.png", dpi=300, bbox_inches='tight')

    def phonetype_counts(self, freqs):
        counts = Counter()
        for c1, c2 in freqs:
            n, v = 'A', 'A'
            if c1 in plosives:
                n = 'P'
            elif c1 in nasals:
                n = 'N'
            if c2 in plosives:
                v = 'P'
            elif c2 in nasals:
                v = 'N'
            counts[n + v] += 1
        counts = dict(counts.most_common(6))
        return counts

    def preprocess_work(self, imode, collection, work):
        sents = []
        text = root + imode + "/" + collection + "/" + work + ".txt"
        with open(text, encoding="utf8") as input:
            for sent in input.readlines():
                sent = re.sub(dropper, "", sent)
                sent = re.sub("\s+", " ", re.sub(punct, " ", sent)).replace("஡஢", "ரி")
                if sent.count(" ") > 2:  # at least two cheers
                    sents.append(sent)
        return sents

    def compute_cfd(self, text, to_merge=True):
        ret = []
        if to_merge:
            text = text.replace(' ', '').replace('\n', '')
        else:
            text = text.replace('\n', ' ')
        for pos in range(len(text) - 2):
            if text[pos] in con and text[pos + 1] == pulli and text[pos + 2] in con:
                ret.append((iso[text[pos]], iso[text[pos + 2]]))
        return ret


p = MayalProcessor()

collections = ["எட்டுத்தொகை", "பத்துப்பாட்டு"]
works = {
    "எட்டுத்தொகை": ["ஐங்குறுநூறு", "அகநானூறு", "கலித்தொகை", "குறுந்தொகை", "நற்றிணை", "பரிபாடல்", "பதிற்றுப்பத்து",
                    "புறநானூறு", "எட்டுத்தொகை"],
    "பத்துப்பாட்டு": ["திருமுருகாற்றுப்படை", "பொருநராற்றுப்படை", "சிறுபாணாற்றுப்படை", "பெரும்பாணாற்றுப்படை",
                      "முல்லைப்பாட்டு", "மதுரைக்காஞ்சி", "நெடுநல்வாடை", "குறிஞ்சிப்பாட்டு", "பட்டினப்பாலை",
                      "மலைபடுகடாம்", "பத்துப்பாட்டு"]}
imodes = ["சொற்பிரிப்பு", "யாப்பு"]
for collection in collections:
    for work in works[collection]:
        for imode in imodes:
            p.process(imode, collection, work)
