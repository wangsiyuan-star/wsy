
#code:utf-8

"""王思媛 20201028
   用迭代器方法实现斐波那契数列"""

class Fibonacci():    #创建斐波那契迭代器
    def __init__(self,n):    #初始化
        self.n = n
        self.a = 1
        self.b = 0
        self.count = 0
        
    def __iter__(self):    #定义iter
        return self
    
    def __next__(self):     #定义next
        while self.count < self.n:
                self.a,self.b = self.b,self.a+self.b
                self.count += 1
                return self.a

fib = Fibonacci(10)    #调用斐波那契迭代器
for i in range(10):    #遍历迭代器
    print(next(fib),end = " ")

