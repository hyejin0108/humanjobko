# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 10:39:27 2026

@author: User
"""
# r: 읽기 w:쓰기 a: append 추가로 쓰기
with open(file="test", mode="w", encoding="utf-8") as f:
    f.write("파이썬\n")
    f.write("이다\n")


with open(file="test", mode="a", encoding="utf-8") as f:
    f.write("추가로 쓴다.\n")


with open(file="test", mode="r", encoding="utf-8") as f:
    for line in f:
        print(line)

 #%%
 a = 10
 print(f"{a:^{a}}잔")