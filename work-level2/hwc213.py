# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。


示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
它们的二进制表示中有两个位不同，所以汉明距离为 2。
'''

def TEST_DO_NOT_CHANGE(x,y):
    print(x,y)
    rlt = None
    ##########start下面可以改动
    #首先肯定是给十进制转换成二进制，套两个循环一个就是在x的里面循环另一个在y里面循环
    #需要转化成二进制，就是bin然后去掉ob
    x= bin(x)[2:]
    y = bin(y)[2:]
    #需要给它补全来对齐
    length = max(len(x),len(y))
    x = x.zfill(length)
    y = y.zfill(length)
    rlt = 0
    for i in range(0,length):
        if x[i]!=y[i]:
            rlt = rlt+1






    
    return rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE(1,4))
