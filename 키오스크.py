# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 11:16:06 2026

@author: User
"""

#%% 실습1
name = input("이름을 입력하세요:")
print("어서오세요 {name}님")
menu_number = int(input("주문할 메뉴를 선택하세요 (예시: 2)"))
quantity = int(input(">주문 수량을 입력하세요.: "))

#%% 실습2
window_width = 40;
store_name = "별다방"
welcome_msg = f"어서오세요. {store_name}입니다."

print('-'*window_width)
print(welcome_msg.center(window_width-11)) # 글자수 빼기
print('-'*window_width)

#%% 최종

# 1. 인삿말 출력하기
window_width = 40
store_name = "별다방"
welcome_msg = f"어서오세요. {store_name}입니다."

print('-'*window_width)
print(welcome_msg.center(window_width-11)) # 글자수 빼기
print('-'*window_width)


#3. Menu
menu_names = ['Americano','Latte','Juice']
price_dict = {'Americano':3500,
              'Latte':4000,
              'Juice':4500
              }
inventory_dict = {'Americano':10,
                  'Latte':5,
                  'Juice':7
                  }
menu_format = '%2d. %10s %5d원 ( %3d 잔 )'
print('[Menu]'.center(window_width))
print('-'*window_width)
for i in range(3):
    menu_name = menu_names[i]
    print(menu_format%(i+1, menu_name, price_dict[menu_name], inventory_dict[menu_name]))
print('-'*window_width)

# 3. cart 생성 및 메뉴 입력받기
cart = dict()

for name in menu_names:
    cart[name] = 0

print(cart)

add_cart_msg = "* 장바구니에 %s %d잔 추가되었습니다."
exceed_cart_msg = "죄송합니다. 현재 %s는 %d잔까지 주문 가능합니다."

menu_number = int(input("주문할 메뉴를 선택하세요 (예시: 2) "))
menu_name = menu_names[menu_number-1]

quantity = int(input(">주문 수량을 입력하세요.: "))

is_vaild = inventory_dict[menu_name] >= quantity

if is_vaild:
    print(add_cart_msg%(menu_name, quantity))
    cart[menu_name] += quantity
else:
    print(exceed_cart_msg%(menu_name, inventory_dict[menu_name]))