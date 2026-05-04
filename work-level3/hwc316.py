# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整


题目
给定一个二进制数组， 计算其中最大连续 1 的个数。

 

示例：

输入：[1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.





'''
#from mkl_random.mklrand import length


def TEST_DO_NOT_CHANGE(nums):
    print(nums)
    rlt = None
    ##########start下面可以改动
    #依旧是双指针，滑动chaungkou
    pos = 0
    leng = 0

    if len(nums) ==0:
        rlt =0
    for i in range(len(nums)):
        if nums[i] != 1:
            pos = i+1
            i=i+1
        else :
            pos = pos

        leng = max(leng,i-pos+1) #没有涉及到i+1的元素所以其实还是用i
        rlt = leng



    
    return rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([1,1,0,1,1,1]))
