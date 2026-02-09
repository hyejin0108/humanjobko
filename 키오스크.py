welcome_msg = "어서오세요, %s입니다."
input_menu_number_msg = "> 주문할 메뉴를 선택하세요. (예시. 2): "
input_quantity_msg = "> 수량을 입력하세요"
exit_cart_msg = "* Enter를 누르면 장바구니로 이동합니다."
input_menu_msg = "> 주문할 메뉴를 선택하세요. (예시. 1): "
exceed_stock_msg = "죄송합니다. 현재 %s는 %d만큼 주문가능합니다."
add_cart_msg = "* 장바구니에 %s %d잔이 추가되었습니다."
complete_order_msg = "주문이 완료되었습니다."
complete_sale_msg = "영업이 종료되었습니다."

window_width = 40
income = 0
store_name = "별다방"
menu_names = ["Americano", "Latte", "Juice"]
stock_dict = {"Americano":10,
              "Latte":7,
              "Juice":5
              }
price_dict = {"Americano":3500,
              "Latte":4000,
              "Juice":4500
              }

def print_div_line():
    print("-"  * window_width)

def input_menu():
    menu_number = input(input_menu_msg)
    if menu_number == "":
        return -1
    else:
        return int(menu_number) - 1
def quantity_stock_vaildity(quantity, menu_name):
    return stock_dict[menu_name] >= quantity
    

while sum(stock_dict.values()) > 0:
    
    # 메뉴판 출력
    print_div_line()
    print((welcome_msg%(store_name)).center(window_width-len(store_name)-8))
    print_div_line()
    print("[Menu]".center(window_width))
    print_div_line()

    for idx, name in enumerate(menu_names):
        print(f"{idx+1}. {name:>10} {price_dict[name]:>5}원 ({stock_dict[name]:>3}잔)")
    print_div_line()
    
    cart = {name : 0 for name in menu_names}
    
    while True:
        print(exit_cart_msg)
        menu_number = input_menu()
        menu_name = menu_names[menu_number]
    
        if menu_number == -1: # 주문 완료
        
            for name, quantity in cart.items():
                income += price_dict[name] * quantity
                stock_dict[name] -= quantity
                
            del cart
            
            print(complete_order_msg)
            break
        else:
            while True:
                quantity = int(input(input_quantity_msg))
                if quantity_stock_vaildity(quantity, menu_name):
                    cart[menu_name] += quantity
                    print(add_cart_msg%(menu_name, quantity))
                    break
                else:
                    print(exceed_stock_msg%(menu_name, stock_dict[menu_name]))
print_div_line()
print(complete_sale_msg)
print_div_line()
print("영업 매출: " + str(income))
            
            
                
        
    


    