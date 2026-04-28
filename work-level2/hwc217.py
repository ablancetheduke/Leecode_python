# -*- coding: utf-8 -*-
'''
函数代码请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
给一个不多于5位的正整数，要求：一、求它是几位数(结果仅需输出阿拉伯数字)，二、逆序打印出各位数字。
请将最终结果合并保存到lst_rlt列表中。

输出结果示例：54321的输出结果为[5, 1, 2, 3, 4，5]，其中首位的5表示总位数，自第二个元素起依次为该正整数的个、十、百、千、万位数字。
程序分析：学会分解出每一位数。　
'''


def TEST_DO_NOT_CHANGE(num_input):
    lst_rlt = []
    print(num_input)

    ##########start下面可以改动
    # 判断输入是否合法
    if num_input > 99999 or num_input <= 0:
        print("请输入不多于5位的正整数")
    else:
        # 计算逆序的数字并保存
        while num_input > 0:
            lst_rlt.append(num_input % 10)
            num_input //= 10

        # 添加总位数
        lst_rlt.append(len(lst_rlt))

        # 逆序lst_rlt，使得第一个元素是位数
        lst_rlt = lst_rlt[::-1]
    ##########end上面可以改动

    return lst_rlt


if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE(54321))
    #######下面可以添加测试语句
    
