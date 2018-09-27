
# coding: utf-8

# In[1]:

print("selam ben cuberen")


# In[2]:

var_0 = 10
var_1 = 100


# In[3]:

var_1


# In[4]:

print(var_1)


# In[5]:

s1 = "eren"
s2 = "k"


# In[6]:

s1+s2


# In[7]:

print(s1+s2)


# In[9]:

s1[1]


# In[12]:

s3= "5"


# In[13]:

s3


# In[14]:

int(s3)


# In[22]:

import random
myList = []
for i in range(10):
    s = random.randint(0,1000000)
    myList.append(s)
print(myList)


# In[34]:

def createArray(s):
    myList = []
    for i in range(s):
        myList.append(random.randint(0,10))
    return myList
def createArrayVersion(s):
    myList = np.arange(s)
    return myList
def printArray(array):
    print(array)
def incArray(array):
    myList_1 = []
    for i in array:
        myList_1.append(i+1)
    return myList_1


# In[30]:

dizi_1 = createArray(30)
printArray(dizi_1)
dizi_2 = incArray(dizi_1)
printArray(dizi_2)


# In[33]:

import numpy as np
x= np.arange(10)
x


# In[41]:

myL = createArrayVersion(100000000)
myL+2


# In[42]:

print("*"*50)


# In[43]:

import matplotlib.pyplot as plt


# In[45]:

image_1 = plt.imread("test.jpg")


# In[46]:

plt.imshow(image_1)
plt.show()


# In[47]:

image_1.shape


# In[48]:

type(image_1)


# In[ ]:



