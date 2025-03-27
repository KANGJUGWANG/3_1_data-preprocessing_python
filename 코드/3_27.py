#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## 3월 27일 문제 풀이


# In[ ]:


## 모든 가상환경과 jupyter kernel을 삭제하시오.


# In[ ]:


## DataCG라는 가상환경을 만들고 kernel을 생성하시오.


# In[30]:


## 1,5,7,8,10,"안녕","a"의 값을 가지는 리스트를 생성하시오.
data = [1,5,7,8,10, "안녕", "a"]
print(data, type(data))


# In[ ]:


# 두 배열 [1,2,4,5],[2,3,5,6]의 합을 구하시오.


# In[14]:


pip install numpy
import numpy as np


# In[31]:


arr1= np.array([1,2,4,5])
arr2 = np.array([2,3,5,6])
print(arr1 + arr2)


# In[22]:


#1행[1,2,3,4,5,6], 2행[20,19,18,17,16,15]값을 가지는 배열을 만드시오.
arr = np.array([[1,2,3,4,5,6],[20,19,18,17,16,15]])
print(arr)


# In[28]:


# 아래의 값을 print를 활용해 도출하시오.
print("-"*20)
print("데이터전처리수업")
print("끝")
print("-"*20)


# In[ ]:




