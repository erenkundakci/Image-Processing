#!/usr/bin/env python
# coding: utf-8

# In[112]:


#a) 28x28 boyutunda içeriği 0 ve 1 olan bir matris oluştur
#b) a'da üretilen matriste 1'leri içeren MBR dikdörtgen üreten fonk. yaz
#c) Kendisine aktarılan 2 vektörün benzerliğini return eden fonk. yaz
#d) a'da yazdığımız fonk. kullanarak 100 farklı matris elde et, 1. üretilen matris ile diğerlerini karşılaştırıp benzerliğini listele

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt


# In[113]:


#a'nın cevabı:
def create_matrix_28by28():
    a = np.random.randint(2, size=784)
    return a.reshape(28,28)

matrix28by28 = create_matrix()
print(matrix28by28)


# In[114]:


#b'nin cevabı:
def MBR_create_28by28_with_0and1(matrix_a):
    m = matrix_a.shape[0]
    n = matrix_a.shape[1]
    x_min=m
    x_max=0    #başlangıç değerleri olası en olumsuz durum
    y_min=n
    y_max=0
    
    for i in range(m):
        for j in range(n):
            if(matrix_a[i,j]==1 and x_min > i):    #resim/matris üzerinden
                x_min = i                         #x_min, ... güncelleniyor
            if(matrix_a[i,j]==1 and x_max < i):
                x_max = i
            if(matrix_a[i,j]==1 and y_min > j):
                y_min = j
            if(matrix_a[i,j]==1 and y_max < j):
                y_max = j
    return (x_min,x_max,y_min,y_max)

MBR_create_28by28_with_0and1(matrix28by28)


# In[115]:


#c'nin cevabı:
def get_matrix_similiarity(matrix_a, matrix_b):
    m=matrix_a.shape[0]
    n=matrix_a.shape[1]
    similiarity=0
    for i in range(m):
        for j in range(n):
            similiarity = similiarity + matrix_a[i,j]* matrix_b[i,j]
    return similiarity
    
get_matrix_similiarity(create_matrix_28by28(), create_matrix_28by28())


# In[122]:


#d'nin cevabı:
def get_100matrix_similiarity():
    first_matrix = create_matrix_28by28()
    matrix_array = []
    for i in range(99):
        matrix_array.append(create_matrix_28by28())
    
    result_array=[]
    result_array.append(get_matrix_similiarity(first_matrix, first_matrix)) #1. üretilen matris kendisiyle karşılaştırıldığında benzerliği en fazla olan olmalı.
    for j in matrix_array:
        result_array.append(get_matrix_similiarity(first_matrix, j))
        
    return result_array
        
print(get_100matrix_similiarity())


# In[ ]:




