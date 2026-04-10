#!/usr/bin/env python
# coding: utf-8

# In[13]:


import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


# In[14]:


import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pandas as pd


# In[15]:


nltk.download('punkt_tab')
nltk.download('stopwords')


# In[16]:


data = pd.read_csv("tripadvisor_hotel_reviews.csv")


# In[17]:


data.info()
data.head()
data['Review'][1]


# In[18]:


data['review_lowercase'] = data['Review'].str.lower()


# In[19]:


en_stopwords = stopwords.words('english')
en_stopwords.remove("not")


# In[20]:


data['review_no_stopwords'] = data['review_lowercase'] .apply(lambda x: ' '.join([word for word in x.split() if word not in
en_stopwords]))


# In[21]:


data['review_no_stopwords_no_punct'] = data.apply(
lambda x: re.sub(r"[*]", "star", x['review_no_stopwords']), axis=1)


# In[22]:


data['tokenized'] = data.apply(
lambda x: word_tokenize(x['review_no_stopwords_no_punct']), axis=1)


# In[23]:


ps = PorterStemmer()
data["stemmed"] = data["tokenized"].apply(lambda tokens: [ps.stem(token) for
token in tokens])


# In[24]:


lemmatizer = WordNetLemmatizer()
data["lemmatized"] = data["tokenized"].apply(lambda tokens:
[lemmatizer.lemmatize(token) for token in tokens])


# In[25]:


tokens_clean = sum(data['lemmatized'], [])


# In[26]:


unigrams = pd.Series(nltk.ngrams(tokens_clean, 1)).value_counts()


# In[27]:


bigrams = pd.Series(nltk.ngrams(tokens_clean, 2)).value_counts()


# In[28]:


ngrams_4 = pd.Series(nltk.ngrams(tokens_clean, 4)).value_counts()


# In[29]:


data[['Review','tokenized','stemmed','lemmatized']].head()


# In[30]:


unigrams.head(10)
bigrams.head(10)
ngrams_4.head(10)


# In[ ]:




