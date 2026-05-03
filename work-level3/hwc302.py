'''
请只在 "
##########start 下面可以改动

##########end 上面可以改动 "
此题在期中考试考察范围内，作业需提交

中间部分作答，作答行数自由调整


题目：括号匹配

编写一个 Python 函数，用于检查给定的字符串中的括号是否匹配。字符串中允许包含小括号 ()、中括号 [] 和大括号 {}，并且括号可以嵌套。

检查时，要确保每个左括号都有与之匹配的右括号，并且括号的嵌套关系必须正确。例如，字符串 "()[]{}" 是括号匹配的，而字符串 "{[()]}" 也是括号匹配的，但字符串 "{[)]}" 不是括号匹配的。

请编写一个函数 TEST_DO_NOT_CHANGE(s)，其中 s 是输入的字符串，函数应该返回布尔值，表示括号是否匹配。
'''
def TEST_DO_NOT_CHANGE(s):
    stack = []  # 使用栈来辅助判断括号匹配
    ##########start下面可以改动
    #如果stack还有剩余，那么这个就是会有False，所以都是用pop给它弹出去，我感觉依旧是双指针
    pos = 0
    # for i in range(len(s)):
    #     if s[i] =='(' or s[i] =='[' or s[i] =='{':
    #         stack.append(s[i])
    #     elif s[i] ==')':
    #         if s[i-1] =='(':
    #             stack.pop()
    #     elif s[i] ==']':
    #         if s[i-1] =='[':
    #             stack.pop()
    #     elif s[i] == '}':
    #         if s[i - 1] == '{':
    #             stack.pop()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        elif ch == ')' or ch == ']' or ch == '}':
            if not stack:
                return False
            if stack[-1] != pairs[ch]:
                return False
            stack.pop()

    return not stack  # 最后栈中应该为空


# def TEST_DO_NOT_CHANGE(s):
#     stack = []
#
#     for ch in s:
#         if ch == '(' or ch == '[' or ch == '{':
#             stack.append(ch)
#
#         elif ch == ')':
#             if not stack:
#                 return False
#             if stack[-1] == '(':  #这个stack[-1]就是最左边的元素可以不用一个指针指着，每一次都是最左边就行了
#                 stack.pop()
#             else:
#                 return False
#
#         elif ch == ']':
#             if not stack:
#                 return False
#             if stack[-1] == '[':
#                 stack.pop()
#             else:
#                 return False
#
#         elif ch == '}':
#             if not stack:
#                 return False
#             if stack[-1] == '{':
#                 stack.pop()
#             else:
#                 return False
#
#     return not stack

if __name__ == "__main__":
    print(TEST_DO_NOT_CHANGE("()[]{}"))  # 应该输出 True
    print(TEST_DO_NOT_CHANGE("{[()]}"))  # 应该输出 True
    print(TEST_DO_NOT_CHANGE("{[)]}"))  # 应该输出 False