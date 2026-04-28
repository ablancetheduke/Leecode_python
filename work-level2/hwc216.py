# -*- coding: utf-8 -*-
'''
函数代码请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
求0—7所能组成的奇数个数。 　
程序分析：
组成1位数是4个。
组成2位数是7*4个。
组成3位数是7*8*4个。
组成4位数是7*8*8*4个。
输入是 n  n为几位数
输出是 奇数个数  
如 输入 n=4
输出的 rlt_sum=7*8*8*4
'''

def TEST_DO_NOT_CHANGE(n):
    rlt_sum = None
    ##########start下面可以改动
    #这个比较简单，如果是n=1,就是4，n= 2就是，其余的就是别的
    if n == 1:
        rlt_sum = 4;
    elif n ==2:
        rlt_sum = 7*4;
    else :
        rlt_sum = 7*8**(n-2)*4;


  
    
    return rlt_sum

    
if __name__ == "__main__":
    print (TEST_DO_NOT_CHANGE(4))
    #######下面可以添加测试语句
    
