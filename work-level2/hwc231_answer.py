# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
给定一个字符串来代表一个学生的出勤记录，这个记录仅包含以下三个字符：

'A' : Absent，缺勤
'L' : Late，迟到
'P' : Present，到场
如果一个学生的出勤记录中不超过一个'A'(缺勤)并且不超过两个连续的'L'(迟到),那么这个学生会被奖赏。

你需要根据这个学生的出勤记录判断他是否会被奖赏。

示例 1:

输入: "PPALLP"
输出: True
示例 2:

输入: "PPALLL"
输出: False

'''
from itertools import count


def TEST_DO_NOT_CHANGE(str_1):
    print(str_1)
    rlt = None
    ##########start下面可以改动
    #这个应该是滑动窗口或者是双指针的事情了，但是我很疑惑的事情是为什么都是两个要求,这个是不是可以简化成不能有多于一个的A，以及不能有字符串“LL”
    count = 0
    for i in str_1:
        if i == "A":
            count = count+1

        if count >1 or "LL" in str_1:
            rlt = True



    return rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE("PPALLP"))
