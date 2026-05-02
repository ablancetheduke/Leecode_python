# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目:
寻找峰值，给出峰值在列表中的索引值; 峰值元素是指其值严格大于左右相邻值的元素，峰值元素不会出现在首尾。
例如nums = [1, 2, 1, 3, 5, 6, 4, 3, 7, 3, 8]，其中峰值为2、6、7这三个元素，最后输出这三个峰值的索引值即 :[1, 5, 8]。
现有以下几个列表，分别找出其中的峰值并输出峰值在其列表中的索引号。
num1 = [2,4,3,1,3,5,8,1,4,1,2]
num2 = [2,1,3,1,2,7,2,3,2,5,6]
num3 = [9,2,1,1,3,2,8,1,1,3,6]
'''

def TEST_DO_NOT_CHANGE(nums):
    print(nums)
    ##########start下面可以改动
    #这个感觉比较简单了，就是先排除第一个 i=0以及第二个i = len(nums)-1,然后判断就是这个
    result = []
    for i in range(1,len(nums)-1):
        if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
            print(nums[i])
            result.append(i)


   
    
    return result
if __name__ == "__main__":
    num1 = [2,4,3,1,3,5,8,1,4,1,2]
    num2 = [2,1,3,1,2,7,2,3,2,5,6]
    num3 = [9,2,1,1,3,2,8,1,1,3,6]
    print(TEST_DO_NOT_CHANGE(num1)) 
    print(TEST_DO_NOT_CHANGE(num2)) 
    print(TEST_DO_NOT_CHANGE(num3)) 