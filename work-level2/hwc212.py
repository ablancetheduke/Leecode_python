# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
现有两个没有重复元素的数组nums1和nums2，其中nums1是nums2的子集。

请你找出nums1中每个元素在nums2中的下一个比其大的值。

nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于num1中的数字1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于num1中的数字2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。


'''


def TEST_DO_NOT_CHANGE(nums1, nums2):
    print(nums1, nums2)
    lst_rlt = []
    ##########start下面可以改动
    for num in nums1:
        # 在 nums2 中找到当前 num 的位置
        index_in_nums2 = nums2.index(num)
        # 从当前位置向右遍历，找下一个比 num 大的元素
        found = False
        for i in range(index_in_nums2 + 1, len(nums2)):
            if nums2[i] > num:
                lst_rlt.append(nums2[i])
                found = True
                break
        if not found:
            lst_rlt.append(-1)

    ##########end上面可以改动
    return lst_rlt


if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([4, 1, 2], [1, 3, 4, 2]))
