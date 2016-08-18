#!/usr/bin/env python
# -*- coding: utf-8 -*-
#第一行定义了脚本的运行方式为Python
#第二行表明文件存储为UTF-8格式，支持中文

import sys # sys.stdin, sys.stdout

# 输入从标准输入获取
for line in sys.stdin:
    # 去除行首行尾的空格
    line = line.rstrip()
    # 分割字符
    words = line.split()
    # 如上面所说，将word输出，Hadoop为自动将其认为成键值对
    for word in words:
        print "%s\t%s"%(word, 1)
