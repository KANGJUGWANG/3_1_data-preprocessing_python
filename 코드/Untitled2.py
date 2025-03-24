#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=1
b=2
c=3
d=4


# In[3]:


a+b,a-b,a*c


# In[5]:


a+b
a-b
a*c


# In[7]:


print(a+b,a-b,a*c)


# In[13]:


print(a*b,a**b ,d/b,d//b,d%b)


# In[21]:


a= input()
print(type(a))
a = float(a)
print(type(a))
a = int(a)
print(type(a))


# In[22]:


a=1
b=-2
c=0
print(type(a),type(b),type(c))


# In[23]:


a=1.55e3
print(a)


# In[27]:


a=2
b=3
print(a*b,a/b,a**b,a//b,a%b)


# In[28]:


a<b


# In[30]:


print(a<=b,a>=b)


# In[37]:


print(bool(False))


# In[39]:


"Life is too short, You need Python"


# In[49]:


a = "python"
b = "to"
a+b
a*2


# In[50]:


# 데이터의 구조 
# 같은 유형은 데이터 스칼라->벡터->행렬->배열->리스트
# 다른 유형의 데이터 데이터 프레임->리스트
#
# 스칼라(1차원) = 단일값
# 데이터 프레임 = 다른 타입의 벡터로 구성된 행렬
# 리스트  = 최상위 데이터 집합


# In[51]:


li = [1,2,3,4,5]
type(li)


# In[54]:


li2 = ["하나",2,True]
print(type(li2),'\n',li2,li2[0],li2[1],li2[2])


# In[61]:


A = [10,20,30]
B = [20,40,60]
print(A+B)


# In[67]:


import numpy as np


# In[70]:


## 1차원 배열(벡터)
a = np.array([1,2,3])
b = np.array([5,6,7])
c = a+b
print(c,'\n',type(c),'\n',c.shape)


# In[72]:


## 리스트 
a= [1,2,3]
b= [4,5,6]
c=a+b
print(c,'\n',type(c),'\n')


# In[73]:


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[5,6,7],[8,9,10]])
c = a+b
print(c,'\n',type(c),'\n',c.shape)


# In[74]:


a = np.array([[[1,2,3],[4,5,6]]])
b = np.array([[[5,6,7],[8,9,10]]])
c = a+b
print(c,'\n',type(c),'\n',c.shape)

