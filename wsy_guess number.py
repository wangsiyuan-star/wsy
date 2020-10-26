import random    #加载random包


def number():
    a = random.randint(0,100)
    #生成0，100的整数随机数
    
    count = 1
    
    try:
        num = int(input('猜一个数字:'))
        
        while num != a:


            if num > a:
                print('大了')

            else:
                print('小了')

            num = int(input('猜一个数字:'))
            count += 1

        print("\n总共猜了"+ str(count)+'次')
    
    except:
        print("输入有误！")

number()


    
