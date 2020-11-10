#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

origin_mat = np.array([[0,1,5,999,3],
                      [999,0,2,999,999],
                      [999,999,0,999,-4],
                      [999,999,2,0,999],
                      [999,999,999,3,0]])


# In[2]:


#用ford算法生成最短路

def ford(origin_mat):
    
    dimension = origin_mat.shape    #初始化
    front_point = np.ones(dimension[0],dtype = int)
    front_point[0] = -1
    mark_mat = front_point
    weight = origin_mat[0]
#     print(mark_mat)
#     print(weight)
#     print("\n")

    for k in range(dimension[0]):
        for i in range(dimension[0]):
            for j in range(dimension[0]):
                if weight[i] + origin_mat[i,j] < weight[j]:
                    weight[j] = weight[i] + origin_mat[i,j]
                    mark_mat[j] = i+1
                    
    print(mark_mat)
    print(weight) 
    return mark_mat,weight

              
    


# In[3]:


#输出点1到各点的最短路的路径以及路径长度

def print_path(mark_mat,weight):
    
    dimension = mark_mat.shape
    for i in range(0,dimension[0]):
        path = []
        index = i

        while True:
            if index == -2:
                break
            path.append(int(index + 1))
            index = int( mark_mat[index]-1)
            
        print("1--->"+str( int(i + 1) ),end = " : ")
        print(list(reversed(path)))
        print(f"总路长是{weight[i]}")


# In[4]:


mark_mat,weight =ford(origin_mat)

print_path(mark_mat,weight)

