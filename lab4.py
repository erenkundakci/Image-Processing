#!/usr/bin/env python
# coding: utf-8

# In[83]:


import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import os

os.chdir("E:\\!my_eren\\Eren Belgeler\\COMU\Odev\\4. sinif\\1. donem\\Goruntu Isleme\\python codes")

image_rgb = plt.imread("test_3.jpg")
print(image_rgb.shape)
plt.imshow(image_rgb)
plt.show()


# In[42]:


def get_distance(v,weight=[1/3,1/3,1/3]):
    a,b,c = v[0], v[1], v[2]
    w1,w2,w3 = weight[0], weight[1], weight[2]
    return ((a**2)*w1 + (b**2)*w2 + (c**2)*w3)**.5

my_RGB = [1,2,3]
gray_level = get_distance(my_RGB)
print(gray_level)


# In[84]:


def rgb_to_graylevel(image_rgb):
    m,n = (image_rgb.shape[0],image_rgb.shape[1])

    image_graylevel = np.zeros((m,n))
    image_graylevel.setflags(write=1)

    for i in range(m):
        for j in range(n):
            #image_graylevel[i,j] = sqrt((image_rgb[i,j,0]*.3)**2 + (image_rgb[i,j,1]*.3)**2 + (image_rgb[i,j,2]*.4)**2)
            image_graylevel[i,j] = get_distance(image_rgb[i,j,:])

    return image_graylevel
       

#plt.imshow(rgb_to_graylevel(image_rgb))
image_graylevel = rgb_to_graylevel(image_rgb)
plt.imshow(image_graylevel, cmap='gray')
plt.show()


# In[103]:


def graylevel_to_blackwhite(image_graylevel, threshold):
    m,n = (image_graylevel.shape[0], image_graylevel.shape[1])
    
    image_blackwhite = np.zeros((m,n))
    image_blackwhite.setflags(write=1)
    
    for i in range(m):
        for j in range(n):
            if (image_graylevel[i,j] > threshold):
                image_blackwhite[i,j] = 1
            else:
                image_blackwhite[i,j] = 0
    
    return image_blackwhite
    
image_blackwhite = graylevel_to_blackwhite(image_graylevel, 60)
plt.imshow(image_blackwhite, cmap='gray')
plt.show()


# In[104]:


plt.subplot(1,3,1),plt.imshow(image_rgb)
plt.subplot(1,3,2),plt.imshow(image_graylevel, cmap='gray')
plt.subplot(1,3,3),plt.imshow(image_blackwhite, cmap='gray')


# In[ ]:





# In[ ]:




