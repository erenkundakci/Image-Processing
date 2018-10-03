
# coding: utf-8

# In[52]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
from scipy.stats import skew

get_ipython().magic('matplotlib inline')

#resmi aradığımız dizini değiştirmek için
#import os
#cwd = os.getcwd()
#cwd
#os.chdir("D:\\imageProcessing2018")

image_1 = plt.imread("test_2.jpg")
plt.imshow(image_1)
plt.show()


# In[22]:

def reverse_func(x):
    return 255-x

def reverse_image(image):
    image[:,:,0] = reverse_func(image[:,:,0]) 
    image[:,:,1] = reverse_func(image[:,:,1])
    image[:,:,2] = reverse_func(image[:,:,2])

reverse_image(image_1)

#plt.subplot(1,2,1),plt.imshow(image_1)
#plt.subplot(1,2,2),plt.imshow(255-image_1)


# In[23]:

plt.imshow(image_1)
plt.show()


# In[60]:

def histogram_maker(image):
    h_R={}
    h_G={}
    h_B={}
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,0] in h_R.keys()):
                h_R[image[i,j,0]] += 1
            else:
                h_R[image[i,j,0]] = 1
            if(image[i,j,1] in h_G.keys()):
                h_G[image[i,j,1]] += 1
            else:
                h_G[image[i,j,1]] = 1
            if(image[i,j,2] in h_B.keys()):
                h_B[image[i,j,2]] += 1
            else:
                h_B[image[i,j,2]] = 1
                
    plt.bar(list(h_R.keys()), h_R.values(), color='r') #color yerine r,g,b olabiliyor histogramın rengi olarak
    plt.show()
    
    plt.bar(list(h_G.keys()), h_G.values(), color='g') #color yerine r,g,b olabiliyor histogramın rengi olarak
    plt.show()
    
    plt.bar(list(h_B.keys()), h_B.values(), color='b') #color yerine r,g,b olabiliyor histogramın rengi olarak
    plt.show()
                
histogram_maker(image_1)


# In[59]:

def resim_deger_bul(im_1):
    print("Dimension:" , im_1.ndim)
    print("Shape:" , im_1.shape)
    
    print("\n---Min ve Max---\n")
    print("Min kırmızı renk değeri:" , im_1[:,:,0].min()) #:,:,0 vs. dediğimizde o layer için ayrıca bakıyoruz. iki nokta'lar bütün satır ve bütün sütunu kapsıyor demek
    print("Max kırmızı renk değeri:" , im_1[:,:,0].max())
    print("Kırmızı range:", im_1[:,:,0].max() - im_1[:,:,0].min())
    
    print("Min yeşil renk değeri:" , im_1[:,:,1].min())
    print("Max yeşil renk değeri:" , im_1[:,:,1].max())
    print("Yeşil range:", im_1[:,:,1].max() - im_1[:,:,1].min())
    
    print("Min mavi renk değeri:" , im_1[:,:,2].min())
    print("Max mavi renk değeri:" , im_1[:,:,2].max())
    print("Mavi range:", im_1[:,:,2].max() - im_1[:,:,2].min())
    
    print("\n---Mean, Mode, Median---\n")
    print("Kırmızı için mean:", im_1[:,:,0].mean())
    print("Yeşil için mean:", im_1[:,:,1].mean())
    print("Mavi için mean:", im_1[:,:,2].mean())
    print("")
    print("Kırmızı için mode:", stats.mode(im_1[:,:,0]))
    print("Yeşil için mode:", stats.mode(im_1[:,:,1]))
    print("Mavi için mode:", stats.mode(im_1[:,:,2]))
    print("")
    print("Kırmızı için median:", np.median(im_1[:,:,0]))
    print("Yeşil için median:", np.median(im_1[:,:,1]))
    print("Mavi için median:", np.median(im_1[:,:,2]))
    
    print("\n---Çeyreklikler ve IQR---\n")
    print("Kırmızı için Q1:", np.percentile(im_1[:,:,0], 25))
    print("Kırmızı için Q3:", np.percentile(im_1[:,:,0], 75))
    print("Kırmızı için IQR:",np.percentile(im_1[:,:,0], 75) - np.percentile(im_1[:,:,0], 25))
    print("")
    print("Yeşil için Q1:", np.percentile(im_1[:,:,1], 25))
    print("Yeşil için Q3:", np.percentile(im_1[:,:,1], 75))
    print("Yeşil için IQR:",np.percentile(im_1[:,:,1], 75) - np.percentile(im_1[:,:,1], 25))
    print("")
    print("Mavi için Q1:", np.percentile(im_1[:,:,2], 25))
    print("Mavi için Q3:", np.percentile(im_1[:,:,2], 75))
    print("Mavi için IQR:",np.percentile(im_1[:,:,2], 75) - np.percentile(im_1[:,:,2], 25))
    
    print("\n---Skewness---\n")
    print("Kırmızı için skewness:", skew(im_1[:,:,0]))
    print("Yeşil için skewness:", skew(im_1[:,:,1]))
    print("Mavi için skewness:", skew(im_1[:,:,2]))
    
resim_deger_bul(image_1)
                
    
    


# In[ ]:




# In[ ]:



