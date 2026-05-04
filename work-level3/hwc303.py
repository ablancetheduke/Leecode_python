# -*- coding: utf-8 -*-
'''
函数代码请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交
给定一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。

连续递增的子序列 可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。



示例 1：

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 
示例 2：

输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。

'''



def TEST_DO_NOT_CHANGE(nums):
    print(nums)
    rlt = None
    ##########start下面可以改动
    #就是pos指针是一开始的地方然后就是下一个curr指针，就是可以移动的保证其他一直是要连续的
    if len(nums) == 0:
        rlt = 0
        return rlt
    pos = 0
    length = 1

    for i in range(len(nums)-1):
        if nums[i+1]<= nums[i]:
            pos = i+1
        else:
            pos=pos
        length = max(length,i-pos+2)#这个加2还是蛮神奇的,这里已经涉及到我们已经检查了i+1确实是符合条件的一直增大的所以要加上2
    rlt = length



    return rlt
     
    

    
if __name__ == "__main__":
    nums = [1,3,5,4,7]
    print(TEST_DO_NOT_CHANGE(nums))
    #######下面可以添加测试语句
    
