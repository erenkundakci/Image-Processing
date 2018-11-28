#!/usr/bin/env python
# coding: utf-8

# In[83]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn import datasets
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris()


# In[70]:


data = iris.data
classId = iris.target


# In[74]:


#classlara göre otomatik ayıran kod
number_of_class = 3
class_counter = 1
for j in range(number_of_class):
    for i in range(len(classId)):
        if(classId[i] == class_counter-1):
            print(data[i])
    class_counter+=1


# In[82]:


setosa = data[0:50]
versicolor = data[50:100]
virginica = data[100:150]

sepal_length_setosa = np.mean(setosa[:,0])
sepal_width_setosa = np.mean(setosa[:,1])
petal_length_setosa = np.mean(setosa[:,2])
petal_width_setosa = np.mean(setosa[:,3])

sepal_length_versicolor = np.mean(versicolor[:,0])
sepal_width_versicolor = np.mean(versicolor[:,1])
petal_length_versicolor = np.mean(versicolor[:,2])
petal_width_versicolor = np.mean(versicolor[:,3])

sepal_length_virginica = np.mean(virginica[:,0])
sepal_width_virginica = np.mean(virginica[:,1])
petal_length_virginica = np.mean(virginica[:,2])
petal_width_virginica = np.mean(virginica[:,3])


# In[90]:



fig=plt.figure()
ax=plt.axes(projection='3d')

xdata = iris.data[:,0]
ydata = iris.data[:,2]
zdata = iris.data[:,3]
label = iris.target

# ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
ax.scatter3D(xdata[100:149], ydata[100:149], zdata[100:149], marker = 'o')
ax.scatter3D(xdata[50:99], ydata[50:99], zdata[50:99], marker = 'o')
ax.scatter3D(xdata[0:49], ydata[0:49], zdata[0:49], marker = 'o')


# In[128]:


def get_mu_s():
    mu_0 = [5,2,0]
    mu_1 = [4,4,0]
    mu_2 = [3,2,5]
    
    return mu_0,mu_1,mu_2

def get_distance(mu,point):
    x = mu[0] - point[0]
    y = mu[1] - point[1]
    z = mu[2] - point[2]
    
    return (x**2+y**2+z**2)**0.5

def get_class_for_one_instance(flower):
    mu_s = get_mu_s()
    d_0 = get_distance(mu_s[0], flower)
    d_1 = get_distance(mu_s[1], flower)
    d_2 = get_distance(mu_s[2], flower)
    
    if((d_0 < d_1) and (d_0 < d_2)):
        return "0"
    if((d_1 < d_0) and (d_1 < d_2)):
        return "1"
    if((d_2 < d_1) and (d_2 < d_0)):
        return "2"
    
def my_f_1(s_1=125):
    x = iris.data[s_1][0]
    y = iris.data[s_1][2]
    z = iris.data[s_1][3]
    my_f_1 = [x,y,z]
    r = get_class_for_one_instance(my_f_1)
    print(r)

for i in range(150):
    my_f_1(i)


# In[139]:


def get_flower(i):
    x = iris.data[i][0]
    y = iris.data[i][2]
    z = iris.data[i][3]
    return [x,y,z]

def update_mu():
    hata="none"
    mu_0_counter = 0.0001
    mu_0_sum = 0
    
    mu_1_counter = 0.0001
    mu_1_sum = 0
    
    mu_2_counter = 0.0001
    mu_2_sum = 0
    
    c_1=[]
    c_2=[]
    c_3=[]
    
    for i in range(150):
        my_flower_data = get_flower(i)
        
        f_class = get_class_for_one_instance(my_flower_data)
        hata = "var"
        
        if(f_class == "0"):
            c_1.append(my_flower_data)
            
        if(f_class == "1"):
            c_2.append(my_flower_data)
            
        if(f_class == "2"):
            c_2.append(my_flower_data)
        
    
    return c_1,c_2,c_3

update_mu()


# In[145]:


c_1,c_2,c_3 = update_mu()
print(len(c_1))
print(len(c_2))
print(len(c_3))


# In[ ]:




