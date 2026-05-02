## 双指针

典型例题：225，231（三指针），234

可以解决以下的问题，主要就是：

**有序数据**：如合并两个有序数组、两数之和、3Sum 等。

**滑动窗口问题**：如最长不重复子串、子数组和等。

**链表问题**：如检测环、找中点等。

**快速/慢指针**：通过不同速度的指针移动来解决问题。

**分割/交换操作**：常用于反转、排序等任务。

## 关于转圈，又回到原来的地方

（还没说）



## 技巧

```python
 nums[curr],nums[p1]= nums[p1],nums[curr]
```

这就是在进行交换，等式左边是交换前的位置，等式右边是交换后的位置，这样的话就是不需要temp在中间



## 习题理解（从3开始）

#### 301

```python
```题目
给定一个字符串，请你找出其中不含有重复字符的 最长子串的长度。```
def TEST_DO_NOT_CHANGE(s):
    print(s)
    rlt = None
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
```

1.解题思路是两个指针，end在前面主动向右移动，start在左边不动，然后就是判断end这个代表的是不是和start一样，如果一样就是让start移动到和最后一次出现的地方，从这里在开始，然后更新这个max

2.主要就是这个字典的用法，`tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': 'Manni'} `,这个时候就是可以检索，比如`tinydic[Name] `返回的就是`Runoob`当然这个也是可以修改的，从新赋值就行

3.还有就是更新最大值，不用再使用这个`if` 判断了，直接用max（）函数就行

## 重复：

237
