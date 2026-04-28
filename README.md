作业的位置是
E:\python\homeworks\homeworks



## 技巧

1.将一个数组反转用的就是list[::-1]





## 题目反思

1.hwc218

```python
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
```

If we trigger the "break",then the addtion of j will be stopped ,i will change ,the new i equals the formal i plus one,the we get new circle of j 
