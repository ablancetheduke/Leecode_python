# -*- coding: utf-8 -*-
'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
给定一个数组 prices ，它的第 i 个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
def TEST_DO_NOT_CHANGE(prices):
    print(prices)
    rlt = None
    ##########start下面可以改动
    if not prices:
        return 0

    min_price = prices[0]  # 历史最低买入价
    max_profit = 0  # 最大利润

    for price in prices[1:]:
        # 如果当前价格比历史最低价高，尝试卖出
        profit = price - min_price
        max_profit = max(max_profit, profit)
        # 更新历史最低价
        min_price = min(min_price, price)
    rlt = max_profit

    
    return rlt

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([7,1,5,3,6,4]))
    print(TEST_DO_NOT_CHANGE([7,6,4,3,1]))

