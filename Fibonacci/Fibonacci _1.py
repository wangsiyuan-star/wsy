#!/usr/bin/env python
# coding: utf-8

# In[8]:


#code:utf-8
"""王思媛 2020.10.28
   用循环方法生成斐波那契数列"""

def fibonacci(n):    #定义斐波那契函数，n代表输出斐波那契数列的前n项
    
    a = [0,1]
    for i in range(2,int(n)):
        num = a[i-2] + a[i-1]
        a.append(num)
        i += 1
    
    print(a)    


# In[9]:


fibonacci(10)

