
# coding: utf-8

# In[14]:


mylist=list()
def myfilter(func,seq):
    for num in seq:
        if(num%2==0):
            mylist.append(num)
    return mylist

myfilter(lambda x: x%2==0,[2,3,5,8,10,16])

