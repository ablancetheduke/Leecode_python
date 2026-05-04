# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目:
定义函数，求小于等于自然数num的所有完全数（Perfect number），存入list中，返回这个list
完全数是指所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：
第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28


'''
# def TEST_DO_NOT_CHANGE(num):
#     print(num)
#     lst_rlt = []
#     ##########start下面可以改动
#     #首先就是得找这个数字的所有的公约数，然后就是看看全部累加能不能是自己，这个时候其实就是算到n^0.5的这个循环就行了，然后记录模后的数字
#
#     for j in range(1,num+1):
#         count = 0
#         for i in range(2,int((j**0.5))+1):
#             if j % i ==0:
#                 count = count + i +(j/i)
#             if count ==i:
#                 lst_rlt.append(i)
#
#     return lst_rlt

def TEST_DO_NOT_CHANGE(num):
    print(num)
    lst_rlt = []
    ##########start下面可以改动

    for j in range(2, num + 1):
        total = 0

        for i in range(1, j):
            if j % i == 0:
                total = total + i

        if total == j:
            lst_rlt.append(j)

    return lst_rlt
    
if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE(10000))
    print(TEST_DO_NOT_CHANGE(1000))
    

