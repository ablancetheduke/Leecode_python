# -*- coding: utf-8 -*-
'''
函数代码请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整
请不要使用 input函数 

题目：
查找字符串 str_2 在 str_1 中起始位置(第一次出现), 如果 不存在 返回 -1,-1
如:在字符串abcdefg查找包含cde的字段，将起始位置输出 2,4
'''


from pydeck.io.html import j2_env


def TEST_DO_NOT_CHANGE(str_1,str_2):
    print(str_1,str_2)
    i_start = -1
    i_end = -1
    ##########start下面可以改动
    #想的太简单了，首先得给s2的第一个匹配上然后就是s2的每一个要匹配的上也就是1，2，3，对应在s1的j，j+1，等位置有点复杂,循环的条件就是只有当str_1[i+x]=str_2[j+x]才能继续
    for i in range(len(str_1)):  # 外层循环，遍历 str_1
        if str_1[i] == str_2[0]:  # 如果找到 str_2 的第一个字符
            for j in range(len(str_2)):  # 内层循环，遍历 str_2
                if str_1[i + j] != str_2[j]:  # 如果有不匹配的字符
                    break  # 结束内层循环，跳到外层循环的下一个 i
            else:  # 只有当内层循环没有 break 时，才执行
                # 如果 str_2 完全匹配 str_1 的一部分
                i_start = i
                i_end = i_start + len(str_2) - 1
                break  # 结束外层循环，跳出整个循环



    return i_start,i_end

    
if __name__ == "__main__":
    print (TEST_DO_NOT_CHANGE('abcdefg','cde'))
    #######下面可以添加测试语句
    
