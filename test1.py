# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% cell1
print("hello world")
print("test1")
# shift + enter > 코드실행 줄바꿈
# ctrl + enter > 코드 실행


#%% 문자열 연산
a = "사과"
b = "오렌지"
print(a+' '+b)
print(a * 3)
print(len(a))
print()

#인덱싱과 슬라이싱
# -2 -1
#  0  1
# 사 과
print(a[1])
print(a[-2]) # 사과 -2 -1
print(b[0:3]) #[s:e-1]
print(a[:2])
print(a[0:])

#%% formatting
format_date = "%d년 %d월 %d일 %c요일"
print(format_date % (2026,2,3,'화'))

format_date2 = "%4d년 %2d월 %2d일 %c요일" #자릿수 지정
print(format_date2 % (2026,2,3,'화'))

format_date3 = "{}년 {}월 {}일 {}요일".format(2026,2,6,'화')
print(format_date3)

format_date4 = "{year}년 {month}월 {date}일 {day}요일".format(year=2026,month=2,date=6,day='화')
print(format_date4)

year, month, date, day = 2026,2,6,'화'
format_date5 = f"{year}년 {month}월 {date}일 {day}요일"
print(format_date5)

year, month, date, day = 2026,2,6,'화'
format_date5 = f"{year:4}년 {month:2}월 {date:2}일 {day}요일" #자릿수 지정
print(format_date5)

item = "cake"
print(f"{item:<10} is sold out!") # 정렬 < ^ >
print(f"{item:^10} is sold out!")
print(f"{item:>10} is sold out!")

#정렬 메소드
print(item.ljust(20))
print(item.center(20))
print(item.rjust(20))

#split()

s = "hello world"
print(s.split()) # 모든 공백
print(s.split(' ')) # ' ' 기준

splited_string = s.split()
print(' '.join(splited_string))

#%% 리스트
"""
append(), insert()
pop(), remove()
sort(), reverse()
index(요소) - 위치
count(요소) - 원소 횟수
"""
name = [1,2,3,4]
name.reverse()
print(name)

#%%
immutable = 'apple', 'orange'
immutable = 'change'