
# coding: utf-8

# In[12]:


def myreduce(func, seq):
    max=seq[0]
    for next in seq[1:]:
        if next > max:
            max=next
    return max

myreduce(lambda x: x>y,[1,2,3,4,10])

