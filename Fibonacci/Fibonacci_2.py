#!/usr/bin/env python
# coding: utf-8

# In[18]:


#code:utf_8

"""王思媛 2020.10.28
   用生成器方法实现斐波那契数列"""

    
def fibonacci(n):    #生成器函数
    a,b = 0,1  #斐波那契数列的前两项为0，1
    count = 0
    while True:
        if (count>n):
            break
        else:
            yield a 
            a,b = b,a+b
            count += 1

def print_fibonacci(n):
    f = fibonacci(n)
    for i in range(n):    #使用next()输出斐波那契数列
        print(next(f),end = ' ')    

        


# In[19]:


print_fibonacci(10)

