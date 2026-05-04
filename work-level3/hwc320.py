# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整


题目
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：10

进一步解释，避免歧义
题目是求 区间内最小缺失正整数

给定一个未排序的整数数组 `nums`（数组中可能包含负数和 0）。

请在**正整数序列中**，找出**落在数组中已出现正整数范围内、但未在数组中出现的最小缺失值**，并返回该值。

如果在该正整数范围内不存在缺失的数，则返回该范围之后的下一个正整数。
如果数组中没有出现任何正整数，则返回 1。

———

**示例**

示例 1：
输入：`nums = [1, 2, 0]`
输出：`3`

解释：
数组中出现的正整数是 1 和 2，范围为 1 到 2。
该范围内没有缺失的数，因此返回下一个正整数 3。

———

示例 2：
输入：`nums = [3, 4, -1, 1]`
输出：`2`

解释：
数组中出现的正整数是 1、3、4，范围为 1 到 4。
在该范围内，2 没有出现，因此返回 2。

———

示例 3：
输入：`nums = [7, 8, 9, 11, 12]`
输出：`10`

解释：
数组中出现的正整数是 7、8、9、11、12，范围为 7 到 12。
在该范围内，10 没有出现，因此返回 10。

———

示例 4：
输入：`nums = [7, 8, 9]`
输出：`10`

解释：
数组中出现的正整数是 7、8、9，范围为 7 到 9。
该范围内没有缺失的数，因此返回下一个正整数 10。

———

示例 5：
输入：`nums = [-2, 0, -5]`
输出：`1`

解释：
数组中没有出现任何正整数，因此返回 1。


'''
from debugpy.server.cli import in_range


# def TEST_DO_NOT_CHANGE(nums):
#     print(nums)
#     rlt = None
#     ##########start下面可以改动
#     nums.sort()
#     if nums[len(nums)-1]<=0:
#         rlt =1
#
#     #分为两个一个就是内部缺了元素就给他输出，一个就是全部都是完整的，那么就是说最后一个最大的,while nums[i]>0,nums[i+1] must equals nums[i] plus one
#     for i in range(len(nums)-1):
#         if nums[i]>0:
#             if nums[i+1]!=nums[i]+1:
#                 rlt = nums[i]+1
#                 break
#             else :
#                 rlt = nums[len(nums)-1]+1
#
#     return rlt


def TEST_DO_NOT_CHANGE(nums):
    print(nums)
    rlt = None
    ##########start下面可以改动
    nums.sort()
    postive = []

    for i in range(len(nums)):
        if nums[i]>0:
            postive.append(nums[i])

    if  len(postive) ==0:
        rlt =1

    for i in range(len(postive)-1):
        if postive[i + 1] != postive[i] + 1:
            rlt = postive[i] + 1
            return rlt

    return rlt



if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([1,2,0]))
    print(TEST_DO_NOT_CHANGE([3,4,-1,1]))
    print(TEST_DO_NOT_CHANGE([7,8,9,11,12]))
