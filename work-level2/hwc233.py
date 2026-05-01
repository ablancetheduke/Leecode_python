# -*- coding: utf-8 -*-
'''
函数代码请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
有34个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''


def TEST_DO_NOT_CHANGE():
    i_rlt = None
    ##########start下面可以改动
    # 1. 初始化 1 到 34 号人的列表
    people = list(range(1, 35))

    # 2. 记录当前报数的起始索引位置
    index = 0

    # 3. 循环剔除，直到只剩下最后一个人
    while len(people) > 1:
        # 报数到 3 的人退出（索引增加 2，因为列表弹出后元素会自动前移）
        # 计算公式：(当前索引 + 报数步长 - 1) % 当前人数
        index = (index + 3 - 1) % len(people)
        people.pop(index)

    # 4. 将最后剩下的人的编号赋值给 i_rlt
    i_rlt = people[0]

    return i_rlt
    

    
if __name__ == "__main__":
    print (TEST_DO_NOT_CHANGE())
    #######下面可以添加测试语句
    
