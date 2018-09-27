
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import numpy as np


# In[29]:

im_1 = plt.imread("test.jpg")
plt.imshow(im_1)
plt.show()


# In[52]:

def resim_deger_bul(im_1):
    print("Dimension:" , im_1.ndim)
    print("Shape:" , im_1.shape)
    print("Min kırmızı renk değeri:" , im_1[:,:,0].min()) #:,:,0 vs. dediğimizde o layer için ayrıca bakıyoruz. iki nokta'lar bütün satır ve bütün sütunu kapsıyor demek
    print("Max kırmızı renk değeri:" , im_1[:,:,0].max())
    
    print("Min yeşil renk değeri:" , im_1[:,:,1].min())
    print("Max yeşil renk değeri:" , im_1[:,:,1].max())
    
    print("Min mavi renk değeri:" , im_1[:,:,2].min())
    print("Max mavi renk değeri:" , im_1[:,:,2].max())
resim_deger_bul(im_1)


# In[50]:

im_1[:,:,0] = im_1[:,:,0]+100 # sondaki rakam sırasıyla 0,1,2 - R,G,B'ye karşılık geliyor. Biz burada 0 değerini yani R'yi 100 arttırdık.
plt.imshow(im_1)
plt.show()


# In[54]:

resim_deger_bul(im_1)


# In[ ]:



