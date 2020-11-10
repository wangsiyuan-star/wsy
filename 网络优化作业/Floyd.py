#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
origin_mat = np.array([[0,4,5,999,999],
                       [999,0,3,999,6],
                       [999,999,0,-2,3],
                       [999,1,999,0,999],
                       [-4,999,999,2,0]])


# In[2]:


def floyd(origin_mat):
    dimension = np.shape(origin_mat)    #初始化U矩阵和R矩阵
    u_mat = origin_mat
    r_mat = np.zeros((dimension[0],dimension[0]),dtype = int)
    for i in range(dimension[0]):
            r_mat[i] = list(range(1,dimension[0]+1))
#     print(u_mat)
#     print(r_mat)
    
    for k in range(dimension[0]):
        for i in range(dimension[0]):
            for j in range(dimension[0]):
                if u_mat[i,j] > u_mat[i,k] + u_mat[k,j]:
                    u_mat[i,j] = u_mat[i,k] + u_mat[k,j]
                    r_mat[i,j] = r_mat[i,k]
        
    print(u_mat)
    print(r_mat)
    
    return u_mat,r_mat
    


# In[3]:


floyd(origin_mat)

