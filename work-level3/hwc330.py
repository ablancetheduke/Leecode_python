# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目:《最小差》

问题描述
给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差

示例：

输入：[1, 3, 15, 11, 2], [23, 127, 235, 19, 8]
输出：3

原因：即数值对(11, 8)

'''
def TEST_DO_NOT_CHANGE(lst_1,lst_2):
    result = None
    minmun = 99999
    ##########start下面可以改动
    # #依旧是循环，那这样就是n^2
    # for i in range(len(lst_1)):
    #     for j in range(len(lst_2)):
    #         minmun = min(minmun,abs(lst_1[i]-lst_2[j]))
    #
    # result = minmun
    # lst_1.sort()
    # lst_2.sort()
    #
    i = 0
    j = 0

    while i < len(lst_1) and j < len(lst_2):
        diff = abs(lst_1[i] - lst_2[j])
        minmun = min(minmun, diff)

        if lst_1[i] < lst_2[j]:
            i += 1
        else:
            j += 1

    result = minmun






    ##########end上面可以改动


    return result
          
if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))
