# -*- coding: utf-8 -*-
"""

#Semantic Analysis Using Python - NLP

* Tutorial: http://news.towardsai.net/nls
* Github: https://github.com/towardsai/tutorials/tree/master/natural_language_processing/semantic-analysis.py
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=5, remove=('headers', 'footers', 'quotes'))
df = dataset.data
df

new_df = pd.DataFrame({'document':df})

# removing everything except alphabets
new_df['clean_doc'] = new_df['document'].str.replace("[^a-zA-Z#]", " ")

# removing short words
new_df['clean_doc'] = new_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>4]))

# make all text lowercase
new_df['clean_doc'] = new_df['clean_doc'].apply(lambda x: x.lower())

from nltk.corpus import stopwords
swords = stopwords.words('english')

# tokenization
tokenized_doc = new_df['clean_doc'].apply(lambda x: x.split())

# remove stop-words
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in swords])

# de-tokenization
detokenized_doc = []
for i in range(len(news_df)):
    t = ' '.join(tokenized_doc[i])
    detokenized_doc.append(t)

new_df['clean_doc'] = detokenized_doc

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', max_features= 300, max_df = 0.5, smooth_idf=True)

X = vectorizer.fit_transform(news_df['clean_doc'])

X.shape

from sklearn.decomposition import TruncatedSVD

svd_model = TruncatedSVD(n_components=20, algorithm='randomized', n_iter=120, random_state=100)

svd_model.fit(X)
len(svd_model.components_)

terms = vectorizer.get_feature_names()

for i, comp in enumerate(svd_model.components_):
    terms_comp = zip(terms, comp)
    sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
    print("Topic "+str(i)+": ")
    for t in sorted_terms:
        print(t[0])
        print(" ")
