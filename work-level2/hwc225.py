'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：移动零元素
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:

输入: nums = [0]
输出: [0]

'''
from itertools import count


def TEST_DO_NOT_CHANGE(nums):
    print(nums)
    output = []
    ##########start下面可以改动
    #我有一个想法就是在这个num数组里面，先把所有非零的东西都放在这个output里面，然后就是有一个计数的，有几次0，计算几次然后就是把这个加在后面就行
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0 :
            output.append(nums[i])
        else :
            count = count+1


    while count !=0 :
        output.append(0)
        count = count - 1


    return output

def Answer (nums):
    print(nums)

    pos = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[pos] = nums[i]
            pos=pos+1

    for i in range(pos,len(nums)) :
        nums[i] = 0


#双指针的方法，感觉还是挺厉害的


if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([1,2,1,0,3,0,2,5]))
    print(TEST_DO_NOT_CHANGE([1,0,-1]))
    print(TEST_DO_NOT_CHANGE([0,1]))