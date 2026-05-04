# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整


题目
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

注意 上面的输出只是为了好看，无需输出的list打印出来像上面一样。当然如果你有空，也可以尝试一下!
'''



def TEST_DO_NOT_CHANGE(numRows):
    print(numRows)
    lst_rlt = []
    ##########start下面可以改动
    #这个题目那么难
    for i in range(numRows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = lst_rlt[i - 1][j - 1] + lst_rlt[i - 1][j]

        lst_rlt.append(row)
    return lst_rlt



if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE(5))
    print(TEST_DO_NOT_CHANGE(1))

