
# coding: utf-8

# In[15]:


def longest_word(lst):
    longestword= lst[0]
    for word in lst[1:]:
        if len(word)>len(longestword):
            longestword=word
    return longestword

longest_word(['me','mine','good','very good'])

