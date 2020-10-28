#!/usr/bin/env python
# coding: utf-8

# In[6]:


#code:utf_8
"""王思媛 20201028
   用递归方法实现斐波那契数列"""

def fibonacci(n):    #定义斐波那契函数，返回第n项的数值
    if n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
    
def print_fibonacci(n):    #定义打印函数，输出前n项斐波那契数列
    for i in range(1,n+1):
        print(fibonacci(i),end = ' ' )


# In[8]:


print_fibonacci(10)

