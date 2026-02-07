# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%% 집합
a = [1,2,2,3,3,3,4,4,4,4]
b = set(a)
c = {1,2,2,3,3,4,4,5,5,5}
print(b & c) # 1,2,3,4  교집합
print(b | c) # 합집합(union)
print(c - b) # 차집합(difference)

# 메소드
# 추가 
b.add(17)

b.update([18,19,20,20]) # update(iterable)
print(b)

#삭제
b.remove(18) # 존재하지않는 요소 일시, 에러발생

#%% 논리형 자료
print(bool(0)) # False
bool(1) # 0을 제외한 모든 수

print(bool("")) # False
bool("아무 문자열")

print(bool([])) # False
bool([0]) # 아무 리스트


#%% 논리형 연산
not True
not False

True and False
True and True

False or False
True or False

# > < >= <= == !=

#%% 문자열관련 함수
"이혜진".startswith("이") # 요소로 시작하는지 체크
"이혜진".endswith("혜진") # 요소로 끝나는지 체크

any([True,False,True]) # 하나라도 True면 True
all([True,True,True]) # 다 True여야 True

type(True)