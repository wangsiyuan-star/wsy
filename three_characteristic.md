# 面向对象中类的三大特性


## 1. 继承
继承就是子类继承父类的特征和行为，使得子类对象（实例）具有父类的属性和方法，或子类从父类继承方法，使得子类具有父类相同的行为。
下述例子中先创建一个人类作为父类，人有姓名属性，可以吃饭和睡觉；再创建一个学生类作为子类，学生除了拥有人类的属性，还拥有成绩属性和考试行为。


```python
class People:    #定义父类：人类
    
    def __init__(self,name):    #初始化人类属性：姓名
        self.name = name
        
    def eating(self):
        print(f"{self.name.title()} is eating. ")
        
    def sleeping(self):
        print(f"{self.name.title()} is sleeping.")
        

class Student(People):    #定义子类：学生类
    
    def __init__(self,name,grade):    #定义人类属性，新增学生类属性
        self.name = name
        self.grade = grade
        
    def exam(self):
        print(f"{self.name.title()} got {self.grade} points in recent exam")
        
        
        
lily = Student("lily",90)
lily.eating()
lily.sleeping()
lily.exam()
```

    Lily is eating. 
    Lily is sleeping.
    Lily got 90 points in recent exam
    

## 2. 多态
同一个方法在不同的类中最终呈现出不同的效果，即为多态。


```python
class Animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')
 
 
class People(Animal):
    def run(self):
        print('人正在走')
 
class Pig(Animal):
    def run(self):
        print('pig is walking')
 
 
class Dog(Animal):
    def run(self):
        print('dog is running')

peo1=People()
pig1=Pig()
d1=Dog()
 
peo1.run()
pig1.run()
d1.run()
```

    人正在走
    pig is walking
    dog is running
    

## 3. 封装
把客观的事物封装成抽象的类，并且类可以把自己的数据和方法只让可信的类或者对象操作，对不可信的类进行信息的隐藏。简单的说就是：封装使对象的设计者与对象的使用者分开，使用者只要知道对象可以做什么就可以了，不需要知道具体是怎么实现的。封装可以有助于提高类和系统的安全性。

类内部的变量属性或者函数属性名前加上两个下划线。就实现了对该属性的隐藏，此时，通过外界就查不到该属性。


```python
class Student:
    __school = "suda"

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def tell_info(self):
        print(f"姓名：{self.__name} 学校：{self.__school} 年龄：{self.__age}")
        
        
stu_1 = Student("tom",18)
stu_1.tell_info()
print(stu_1.__school)    #这种方法是查看不到该学校属性的。
```

    姓名：tom 学校：suda 年龄：18
    


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-20-384a6139758d> in <module>
         12 stu_1 = Student("tom",18)
         13 stu_1.tell_info()
    ---> 14 print(stu_1.__school)    #这种方法是查看不到该学校属性的。
    

    AttributeError: 'Student' object has no attribute '__school'



```python
print(stu_1._Student__school)    #采用_类__属性的方法就可以查看了
```

    suda
    


```python
#将人类的姓名变量私有化后，学生类无法调用父类中的私有变量，程序报错

class People:    #定义父类：人类
    
    def __init__(self,__name):    #初始化人类属性：姓名
        self.__name = __name
        
    def eating(self):
        print(f"{self.__name.title()} is eating. ")
        
    def sleeping(self):
        print(f"{self.__name.title()} is sleeping.")
        

class Student(People):    #定义子类：学生类
    
    def __init__(self,__name,grade):    #定义人类属性，新增学生类属性
        self.grade = grade
        
    def exam(self):
        print(f"{self.__name.title()} got {self.grade} points in recent exam")
        
lily = Student("lily",90)
lily.eating()
lily.exam()
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-22-19d6fe57c910> in <module>
         22 
         23 lily = Student("lily",90)
    ---> 24 lily.eating()
         25 lily.exam()
    

    <ipython-input-22-19d6fe57c910> in eating(self)
          7 
          8     def eating(self):
    ----> 9         print(f"{self.__name.title()} is eating. ")
         10 
         11     def sleeping(self):
    

    AttributeError: 'Student' object has no attribute '_People__name'

