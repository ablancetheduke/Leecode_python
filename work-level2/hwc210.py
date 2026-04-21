# -*- coding: utf-8 -*-
'''
函数代码请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？
第10次反弹多高？请将两问的结果（数字）保存到lst_rlt列表并输出。
输出结果示例：[第10次落地时经过的总米数,第10次反弹高度]（输出结果中仅包含阿拉伯数字，不需要单位）
'''
from openpyxl.styles.builtins import total


#from xlwings.pro.reports.filters import height


def TEST_DO_NOT_CHANGE():
    lst_rlt=[]
    ##########start下面可以改动

    h = 100
    total = h
    for i in range(1,10):
        h = h / 2
        total = total +2*h


    lst_rlt.append(total)
    lst_rlt.append(h/2)

    
    return lst_rlt
    
    
    
if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE())
    #######下面可以添加测试语句
    
