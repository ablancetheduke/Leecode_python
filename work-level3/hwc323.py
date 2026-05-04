# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整


题目
整数数组number，判断number中是否存在三个元素a，b，c，使得a + b + c = 0？找出所有满足条件且不重复的三元组。
例如：
number = [-1, 0, 1, 2, -1, -4, 4, -3, 7, -5]
result 形式如下：
[[-5, 1, 4], [-4, -3, 7], [-4, 0, 4], [-3, -1, 4], [-3, 1, 2], [-1, -1, 2], [-1, 0, 1]]
现有如下几个数组：
number1 = [-1, 0, 1, 2, -1, -4, 3]
number2 = [-2, 0, 1, 1, -1, 3, 4]
number3 = [0, -1, 2, -3, 1, 2, 4]
'''
# def TEST_DO_NOT_CHANGE(nums):
#     print(nums)
#     ##########start下面可以改动
#     result = []
#     out = []
#     #我就想的是做一个双循环，然后在剩下的找是不是
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)-1):
#             for z in range(j+1,len(nums)-1):
#                 if nums[i] +nums[j]+nums[z] ==0:
#                     out = [nums[i],nums[j],nums[z]]
#                     out.sort()#排序很重要不然的话就是可能会把这个判断成重复的一个
#
#                     if out not in result:
#                         result.append(out)
#
#
#
#     result.sort()
#     return result
def TEST_DO_NOT_CHANGE(nums):
    print(nums)
    ##########start下面可以改动
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result


if __name__ == "__main__":
    number1 = [-1, 0, 1, 2, -1, -4, 3]
    number2 = [-2, 0, 1, 1, -1, 3, 4]
    number3 = [0, -1, 2, -3, 1, 2, 4]
    print(TEST_DO_NOT_CHANGE(number1))
    print(TEST_DO_NOT_CHANGE(number2))
    print(TEST_DO_NOT_CHANGE(number3))
