#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
import sys

current_word = None # 当前的单词
current_count = 0 # 当前单词的个数

# 输入同样来自于标准输入
for line in sys.stdin:
    line = line.strip()
    parts = line.split('\t')
    # 注意刚刚我们的输出一行仅有两个项，一个为单词，一个为1
    # 所以不满足条件则跳过
    if len(parts) != 2:
        continue
    # 获取当前的word和计数（为1）
    word, count = parts
    # 如果还是当前的单词，则计数加1，否则输出结果，并重置计数
    if current_word == word:
        current_count += 1
    else:
        if current_word:
            print '%s\t%s' % (current_word, current_count)
        current_count = 1
        current_word = word
# 别忘了最后一个输出
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
