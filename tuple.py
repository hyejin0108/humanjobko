# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 19:09:19 2026

@author: User
"""

#%% 튜플 자료형
immutable = ('apple','orange','grape')
immutable = 'apple', 'orange', 'grape'
print(immutable[0])
print(immutable[1])
print(immutable[:-1])
print(immutable[:-2])
# immutable[1] = 'change' # err 재할당 불가능
print(immutable[1])

#%% 3. Menu
window_width = 40
menu_list = ['Americano','Latte','Juice']
price_list = [3500,4000,4500]
inventory_list = [10, 5, 7]
print('[Menu]'.center(window_width))
print('-'*window_width)
for i in range(3):
    print(f'{i+1}. {menu_list[i]:>10} {price_list[i]:6}원 ( {inventory_list[i]:^3}잔 )')
print('-'*window_width)

#%% dictionary
#dict 만들기 1
kor_eng_dic = {'사과':'apple',
               '오렌지':'orange', # key는 문자열
               '바나나':'banana'
               }
apple = ['사과', 'apple']
orange = ['오렌지', 'orange']
banana = ['바나나', 'banana']
#dict만들기 2
print(dict([apple, orange, banana]))

# dict 접근
kor_eng_dic['사과'] # 없는 key 접근 시 에러 발생
kor_eng_dic.get('사과') # 없는 key 접근 시 None

# 메소드
print(kor_eng_dic.items())
print(kor_eng_dic.keys())
print(kor_eng_dic.values())

# 쌍 추가
kor_eng_dic['포도'] = 'grape'
print(kor_eng_dic)

# 쌍 삭제
del kor_eng_dic['포도']
print(kor_eng_dic)

kor_eng_dic.clear() # 모든 값 삭제

#%%
name = [1,2,3,4]
print(name[0:2])