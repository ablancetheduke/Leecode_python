'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：查找质数的和

编写一个 Python 程序，查找并输出从 2 到 n 之间的所有质数的和。

质数是指只能被 1 和自身整除的正整数。例如，2、3、5、7、11 等都是质数。

编写一个函数 TEST_DO_NOT_CHANGE()，它返回从 2 到 n 之间的所有质数的和。

'''
    
def TEST_DO_NOT_CHANGE(num):
    prime_sum = 0
    ##########start下面可以改动
    #我有一个想法就是简单的进行循环，是一个大的循环然后是一个小的循环，但是这样真的时间夫再度就是n*n，有点高，我先写
    for i  in  range (3,num):
        for j in range(2,i):
            if j!=i and i %j ==0:
                break
        else :
            #print(i)
            prime_sum = prime_sum+i

    return prime_sum

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE(100))
    print(TEST_DO_NOT_CHANGE(120))
    print(TEST_DO_NOT_CHANGE(150))
