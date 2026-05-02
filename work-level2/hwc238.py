'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：最高海拔
有一个自行车手打算进行一场公路骑行，这条路线总共由 n + 1 个不同海拔的点组成。自行车手从海拔为 0 的点 0 开始骑行。
给你一个长度为 n 的整数数组 gain ，其中 gain[i] 是点 i 和点 i + 1 的 净海拔高度差（0 <= i < n）。请你返回 最高点的海拔 。

提示：
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

示例 1：

输入：gain = [-5,1,5,0,-7]
输出：1
解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。

示例 2：

输入：gain = [-4,-3,-2,-1,4,3,2]
输出：0
解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。

'''
def TEST_DO_NOT_CHANGE(gain_list):
    output = None
    ##########start下面可以改动
    #这个题目怎么解释呢？那我就先返回海拔高度，然后找最大的就行了,every heigh[i+1] equals heigh[i]+gain_list[i]
    heigh = [0]
    for i in range(len(gain_list)):
        heigh.append(heigh[i]+gain_list[i])

    output = heigh[0]
    for i in range(len(heigh) - 1):
        if heigh[i] > output:
            output = heigh[i]


    
    return output

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE([1,2,1,0,3,0,2,5]))
    print(TEST_DO_NOT_CHANGE([1,0,-1,5,-6,7]))
    print(TEST_DO_NOT_CHANGE([0,1,2,3,-10,7,2]))