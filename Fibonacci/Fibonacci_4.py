
#code:utf-8
"""王思媛 20201028
   用矩阵方法实现斐波那契数列"""

import numpy as np    
                
def fibonacci(n):    #定义斐波那契函数，n表述输出斐波那契的前n位
    fib = [0,1]    #初始化前两项为0，1
    fib_matrix = [[1],[0]]
    parameter_matrix = [[1,1],
                       [1,0]]
    for i in range(n-2):
        fib_matrix = np.matmul(parameter_matrix,fib_matrix)
        fib.append(fib_matrix[0,0])
        
    print(fib)
        
    
fibonacci(10)

