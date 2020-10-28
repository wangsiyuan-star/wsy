#!/usr/bin/env python
# coding: utf-8

# In[16]:


#code:utf_8

"""王思媛 20201028
   用迭代器方法实现斐波那契数列"""

class Fibonacci():
    def __init__(self,n):
        self.n = n
        self.a = 1
        self.b = 0
        self.count = 0
        
    def __iter__(self):
        return self
    
    def __next__(self): 
        while self.count < self.n:
                self.a,self.b = self.b,self.a+self.b
                self.count += 1
                return self.a
                
        

        


# In[17]:


fib = Fibonacci(10)
for i in range(10):
    print(next(fib),end = " ")

