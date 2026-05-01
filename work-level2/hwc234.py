# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [], nums2 = [1]
输出：1.00000

'''

def TEST_DO_NOT_CHANGE( nums1, nums2):
    print(nums1, nums2)
    rlt = None
    ##########start下面可以改动
    #这给就是还是按照原来的从小到大的顺序来合并两个数组，然后返回中间的len+len这种
    #先进行合并,num1是基地数组,有做过红白蓝球的那个，我想先合并在排序,那这样我感觉还是O（n^2）了不够好
    nums1 = nums1+nums2
    pos = 0
    curr = 0

    for i in range(len(nums1)):#还挺神奇，用nums1-1就不行
        if nums1[curr]<nums1[pos]:
            nums1[pos],nums1[curr] = nums1[curr],nums1[pos]
            pos = pos+1
            curr= curr+1
        else :
            curr= curr+1
            pos = curr-1

    if len(nums1)%2 ==0:
        #rlt = (nums1[len(nums1)/2-1]+nums1[len(nums1/2)])/2
        rlt = (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2]) / 2
    else :
        #rlt = nums1[(len(nums1)-1)/2]
        rlt = nums1[len(nums1)//2]

    return rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE( [1,3],[2]))
    print(TEST_DO_NOT_CHANGE([1,2],[3,4]))
    print(TEST_DO_NOT_CHANGE([],[1]))
