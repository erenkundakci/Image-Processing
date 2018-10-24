#!/usr/bin/env python
# coding: utf-8

# In[83]:


import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import os

os.chdir("E:\\!my_eren\\Eren Belgeler\\COMU\\Odev\\4. sinif\\1. donem\\Goruntu Isleme\\python codes")

image_rgb = plt.imread("test_13.png")
print(image_rgb.shape)
plt.imshow(image_rgb)
plt.show()


# In[7]:


def get_distance(v,weight=[1/3,1/3,1/3]):
    a,b,c = v[0], v[1], v[2]
    w1,w2,w3 = weight[0], weight[1], weight[2]
    return ((a**2)*w1 + (b**2)*w2 + (c**2)*w3)**.5


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


# In[85]:


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
    
image_blackwhite = graylevel_to_blackwhite(image_graylevel, 0)
plt.imshow(image_blackwhite, cmap='gray')
plt.show()


# In[31]:


def pixel_compare_external(part_of_image):
    #print(part_of_image.ravel())
    part_of_image = part_of_image.ravel() #2x2 gelen matrisleri 1 boyutlu arraye dönüştürüyoruz
    ones = 0
    zeros = 0
    
    for i in part_of_image:
        if(i == 1):
            ones += 1
        else:
            zeros += 1
            
    if(ones == 3 and zeros == 1):
        return True
        #print(part_of_image, "True")
    else:
        return False
        #print(part_of_image, "False")


# In[33]:


def pixel_compare_internal(part_of_image):
    #print(part_of_image.ravel())
    part_of_image = part_of_image.ravel() #2x2 gelen matrisleri 1 boyutlu arraye dönüştürüyoruz
    ones = 0
    zeros = 0
    
    for i in part_of_image:
        if(i == 1):
            ones += 1
        else:
            zeros += 1
            
    if(ones == 1 and zeros == 3):
        return True
        #print(part_of_image, "True")
    else:
        return False
        #print(part_of_image, "False")


# In[86]:


def count_objects(image_bw):
    m = image_bw.shape[0]
    n = image_bw.shape[1]
    
    E,I = 0,0
    
    for i in range(1, m-1):
        for j in range(1, n-1):
            if(pixel_compare_external(image_bw[i-1:i+1, j-1:j+1])):
                E += 1
            if(pixel_compare_internal(image_bw[i-1:i+1, j-1:j+1])):
                I += 1
                
    print(E,I)
    print("Objects in scene:", (E-I)/4)
            
count_objects(image_blackwhite)


# In[ ]:




