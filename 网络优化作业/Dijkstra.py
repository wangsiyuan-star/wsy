#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
origin_mat = np.array([[999,50,30,40,25],    #初始化图
                       [50,999,15,20,999],
                       [30,15,999,10,20],
                       [40,20,10,999,10],
                       [25,999,20,10,999]])


# In[102]:


def dijkstra(origin_mat):
    dimension = origin_mat.shape 
    #获取矩阵的维数 
     
    try:
        origin_dim = dimension[1]    
        path  = []    #初始化集合 step0
        point_checked = [1]
        point_unchecked = list(range(2,int(origin_dim)+1))
        num_mat = np.zeros((dimension[0], dimension[0]),dtype = int)   
        #初始化集合 step0

        
        while point_unchecked:    #循环运行直至未检查点为空集
            min_num = 999
            for i in point_checked:
                for j in point_unchecked:
                    current_num = origin_mat[i-1,j-1]
                    if current_num < min_num:    #找到未检查点和检查点之间的最短路
                        min_num = current_num
                        point_x = i
                        point_y = j
                             
            point_unchecked.remove(point_y)
            point_checked.append(point_y)
            path.append([point_x,point_y]) 
            num_mat[point_x-1,point_y-1] = current_num
            
            if min_num >= 999:    #如果最小边不存在，最小树不存在
                print("最小树不存在！")
                break
                
    
        print(path)
        print(point_checked)
        print(num_mat)  
    
    except:
        print("输入有误！")



dijkstra(origin_mat)

