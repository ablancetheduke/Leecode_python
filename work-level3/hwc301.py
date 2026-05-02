# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整


题目
给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。

示例：
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

'''
from debugpy.server.cli import in_range


def TEST_DO_NOT_CHANGE(s):
    print(s)
    rlt = None
    ##########start下面可以改动
    #感觉这个是很明显的双指针，我想想得有三个，一个是pos指针，一个是curr指针，一个就是max这个长度，主体是双循环
    # pos  =0
    # curr = 0
    # max = 0
    # for i in range(1,len(s)):
    #     for j in range(pos,curr):
    #         if s[curr]==s[j]:
    #             pos = curr
    #             curr = curr+1
    #             break
    #     else :
    #         curr = curr + 1
    #         if curr-pos>max:
    #             max = curr-pos
    #         else :
    #             max = max

    last_seen = {}
    max_len = 0
    start = 0  # 窗口左边界

    for end in range(len(s)):  # end 是窗口右边界
        # 如果当前字符已经在窗口中出现过
        if s[end] in last_seen and last_seen[s[end]] >= start:
            # 将左边界跳到重复字符上一次出现位置的下一个
            start = last_seen[s[end]] + 1

        # 更新字符最后出现的位置
        last_seen[s[end]] = end
        # 计算当前窗口长度并更新最大值
        max_len = max(max_len, end - start + 1)

    rlt = max_len





    return rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE("abcabcbb"))
    print(TEST_DO_NOT_CHANGE("bbbbb"))
    print(TEST_DO_NOT_CHANGE("pwwkew"))
