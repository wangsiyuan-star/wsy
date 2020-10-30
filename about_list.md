# 作业要求

# 关于Python内置对象类型的“列表list”的综述

- 阐述列表基本知识和应用特点

- 阐述列表与数组之间的异同

- 文中要包含代码演示以及相关的说明

- 语言通顺、术语准确、可读性强

# 1. 列表简介

## 1.1 列表是什么
列表是由一系列特定顺序排列的元素组成。在Python中用方括号（[]）来表示列表，并用逗号（，）来分隔其中的元素。下面是几个简单的示例：



```python
list1 = [1, 2, 3, 4, 5 ]
list2 = ["a", "b", "c", "d"]
list3 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```

## 1.2 访问列表中元素
列表索引从 0 开始，第二个索引是 1，依此类推。通过索引列表可以进行截取、组合等操作。
例如下面的代码可以从列表flowers中提取第一朵花:


```python
flowers = ["jasmine","lily","rose"]
print(flowers[0])
```

    jasmine
    

Python为访问最后一个列表元素提供了一种特殊语法，通过将索引指定为-1，可让Python返回最后一个列表元素;


```python
flowers = ["jasmine","lily","rose"]
print(flowers[-1])
```

    rose
    

索引-2返回倒数第二个列表元素，索引-3返回倒数第三个列表元素，以此类推。

## 1.3 修改列表中的元素
修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可指定列表元素，可指定列表名和要修改的元素的索引，在指定该元素的新值。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

flowers[0] = 'daisy'
print(flowers)
```

    ['jasmine', 'lily', 'rose']
    ['daisy', 'lily', 'rose']
    

## 1.4 在列表中添加元素
### 1.4.1 在列表末尾添加元素
在列表中添加元素时，最简单的方式是将元素附加到列表末尾。
用方法append()给列表附加元素时，它将添加到列表末尾,而不影响列表中的其他所有元素。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)
           
flowers.append('daisy')
print(flowers)
```

    ['jasmine', 'lily', 'rose']
    ['jasmine', 'lily', 'rose', 'daisy']
    

### 1.4.2 在列表中插入元素
使用方法insert()可在列表的任何位置添加新元素，需要指定新元素的索引和值。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

flowers.insert(0,'daisy')
print(flowers)
```

    ['jasmine', 'lily', 'rose']
    ['daisy', 'jasmine', 'lily', 'rose']
    

## 1.5 在列表中删除元素

###  1.5.1 使用del语句删除元素
如果知道要删除的元素在列表中的位置，可以使用del语句。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

del flowers[0]
print(flowers)
```

    ['jasmine', 'lily', 'rose']
    ['lily', 'rose']
    

### 1.5.2 使用方法pop()删除元素
有时候，你要将元素从列表中删除，并接着使用它的值。方法pop()可删除列表末尾的元素，并让你能够接着使用它。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

poped_flower = flowers.pop()
print(flowers)
print(poped_flower)
```

    ['jasmine', 'lily', 'rose']
    ['jasmine', 'lily']
    rose
    

输出表明，列表flowers的最后一个元素已经被删除，它现在存储在变量pope_flower中。

事实上，pop()可以删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

poped_flower = flowers.pop(0)
print(flowers)
print(poped_flower)
```

    ['jasmine', 'lily', 'rose']
    ['lily', 'rose']
    jasmine
    

### 1.5.3 使用方法remove()删除元素
有时候，你不知道要从列表中删除的值所处的位置。如果你只知道要删除的元素的值，可使用方法remove()。


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

flowers.remove('lily')
print(flowers)
```

    ['jasmine', 'lily', 'rose']
    ['jasmine', 'rose']
    

# 2. 列表的应用
## 2.1 遍历列表
在程序编写过程中，经常要遍历列表中的所有元素，对每个元素执行相同的操作。可以使用for循环遍历每个元素：


```python
flowers = ["jasmine","lily","rose"]
print(flowers)

for flower in flowers:
    print(flower)
```

    ['jasmine', 'lily', 'rose']
    jasmine
    lily
    rose
    

##  2.2 列表切片 
要创建切片，可指定要使用的第一个元素的索引和最后一个元素的索引+1（左闭右开）


```python
flowers = ["jasmine","lily","rose","daisy"]
print(flowers[1:3])
```

    ['lily', 'rose']
    

结果输出了列表中索引号为1，2的元素。

如果你没有指定第一个索引，将自动从列表开头开始：


```python
flowers = ["jasmine","lily","rose","daisy"]
print(flowers[:3])
```

    ['jasmine', 'lily', 'rose']
    

要让切片终止于列表末尾，也可以使用类似的语法。


```python
flowers = ["jasmine","lily","rose","daisy"]
print(flowers[1:])
```

    ['lily', 'rose', 'daisy']
    

# 3. 列表(list)与数组(array)的比较

## 3.1 定义
列表(list)是由一系列按特定顺序排列的元素组成，可以将任何东西加入列表中，其中的元素之间没有任何关系。
数组(array)可以紧凑地表示一个基本值的数组：字符，整数，浮点数。数组是序列类型，表现得非常像列表，除了存储在它们中的对象的类型是受约束的。

## 3.2 不同点
### 3.2.1 使用方式不同
list是Python自带的数据类型，不需要预先加载任何包就可以直接使用。



array是Python的一个扩展程序库numpy里的对象，在使用array之前要先加载numpy


```python
list_1 = [1,2,3,4,5]
print(list_1)

import numpy as np
array_1 = np.array([1,2,3,4,5])
print(array_1)
```

    [1, 2, 3, 4, 5]
    [1 2 3 4 5]
    

### 3.2.2 元素类型不同
list中可以存储任何数据类型，也可以包含另一个列表


array的数据成员必须是相同数据类型属性，不同于列表和元组


```python
list_1 = [1,2,3,4,5]
list_2 = ["jasmine","lily","rose","daisy"]
list_3 = [1,2,3,"rose","daisy"]
list_4 = [list_1,list_2,list_3]
print(list_1)
print(list_2)
print(list_3)
print(list_4)

import numpy as np
array_1 = np.array([1,2,3,4,5])
array_2 = np.array(["jasmine","lily","rose","daisy"])
array_3 = np.array([1,2,3,"rose","daisy"])
print(array_1)
print(array_2)
print(array_3)
```

    [1, 2, 3, 4, 5]
    ['jasmine', 'lily', 'rose', 'daisy']
    [1, 2, 3, 'rose', 'daisy']
    [[1, 2, 3, 4, 5], ['jasmine', 'lily', 'rose', 'daisy'], [1, 2, 3, 'rose', 'daisy']]
    [1 2 3 4 5]
    ['jasmine' 'lily' 'rose' 'daisy']
    ['1' '2' '3' 'rose' 'daisy']
    


```python
type(array_1[0])
```




    numpy.int32




```python
type(array_3[0])
```




    numpy.str_




结果显示，array中的int型数字被转化成了字符串

### 3.2.3 使用方式不同
array之间可以进行四则运算，而list不行。


```python
list_1 = [1,2,3,4,5]
list_2 = ["jasmine","lily","rose","daisy"]
list_1+list_2
```




    [1, 2, 3, 4, 5, 'jasmine', 'lily', 'rose', 'daisy']




```python
import numpy as np

array_1 = np.array([1,2,3,4,5])
array_2 = np.array([1,1,1,1,1])
array_1+array_2
```




    array([2, 3, 4, 5, 6])



## 3.3 相同点
list和array都可以通过索引获得元素


```python
list_1 = [1,2,3,4,5]

import numpy as np
array_1 = np.array([1,2,3,4,5])

print(list_1[0])
print(array_1[0])
```

    1
    1
    


```python
list_1 = [1,2,3,4,5]

import numpy as np
array_1 = np.array([1,2,3,4,5])

print(list_1[1:3])
print(array_1[1:3])
```

    [2, 3]
    [2 3]
    
