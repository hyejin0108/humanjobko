welcome_msg = "어서오세요, %s입니다."
input_menu_number_msg = "> 주문할 메뉴를 선택하세요. (예시. 2): "
input_quantity_msg = "> 수량을 입력하세요. "
exit_cart_msg = "* Enter를 누르면 장바구니로 이동합니다."
cancel_cart_msg = "* Enter를 누르면 메뉴 추가가 취소됩니다."
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

#%%
def print_div_line(window_width):
    print("-"  * window_width)

def print_welcome_msg(window_width):
    print_div_line(window_width)
    print((welcome_msg%(store_name)).center(window_width-len(store_name)-8))
    print_div_line(window_width)

def print_menu(window_width, prices, stocks):
    print("-"  * window_width)
    print("[Menu]".center(window_width))
    print_div_line(window_width)
    for idx, name in enumerate(menu_names):
        print(f"{idx+1}. {name:>10} {prices[name]:>5}원 ({stocks[name]:>3}잔)")
    print_div_line(window_width)

def print_cart_transition_msg():
    print(exit_cart_msg)

def print_cancel_msg():
    print(cancel_cart_msg)
    
def print_add_cart_msg(menu_name, quantity):
    print(add_cart_msg%(menu_name, quantity))
    
def print_exceed_msg(menu_name, stocks):
    print(exceed_stock_msg%(menu_name, stocks[menu_name]))

def print_complete_order_msg ():
    print(complete_order_msg)
    
def print_close_store_msg(window_width, income):
    print_div_line(window_width)
    print(complete_sale_msg)
    print_div_line(window_width)
    print("영업 매출: " + str(income))
    
def input_menu():
    menu_number = input(input_menu_msg)
    if menu_number == "":
        return -1
    else:
        return int(menu_number) - 1
    
def input_quantity():
    quantity = input(input_quantity_msg)
    if quantity == "":
        return -1
    else:
        return int(quantity)
    
def is_order(quantity, menu_name, stocks):
    return stocks[menu_name] >= quantity

def is_all_zero_stock(stocks):
    return sum(stocks.values()) > 0

def add_menu(names, prices, stocks, menu_name, price, quantity):
    names.append(menu_name)
    prices[menu_name] = price
    stocks[menu_name] = quantity
def remove_menu(names, prices, stocks, menu_name):
    names.remove(menu_name)
    del stocks[menu_name]
    del prices[menu_name]
    stocks[menu_name] = quantity

def run_store(window_width, names, prices, stocks):
    income = 0
    while is_all_zero_stock(stocks):
        print_welcome_msg(window_width)
        print_menu(window_width, prices, stocks)
        
        cart = {name : 0 for name in menu_names}
        
        while True:
            print_cart_transition_msg()
            menu_number = input_menu()
            menu_name = names[menu_number]
        
            if menu_number == -1: # 주문 완료
            
                for name, quantity in cart.items():
                    income += prices[name] * quantity
                    stocks[name] -= quantity
                    
                del cart
                
                print_complete_order_msg()
                break
            else:
                while True:
                    quantity = input_quantity()
                    if quantity == -1:
                        break
                    elif is_order(quantity, menu_name, stocks):
                        cart[menu_name] += quantity
                        print_add_cart_msg(menu_name, quantity)
                        break
                    else:
                        print_exceed_msg(menu_name, stocks)
    print_close_store_msg(window_width, income)
        
run_store(window_width, menu_names, price_dict, stock_dict)

#%%

while is_all_zero_stock(stock_dict):
    
    # 메뉴판 출력
    print_welcome_msg(window_width)
    print_menu(window_width, price_dict, stock_dict)
    
    cart = {name : 0 for name in menu_names}
    
    while True:
        print_cart_transition_msg()
        menu_number = input_menu()
        menu_name = menu_names[menu_number]
    
        if menu_number == -1: # 주문 완료
        
            for name, quantity in cart.items():
                income += price_dict[name] * quantity
                stock_dict[name] -= quantity
                
            del cart
            
            print_complete_order_msg()
            break
        else:
            while True:
                quantity = input_quantity()
                if quantity == -1:
                    break
                elif is_order(quantity, menu_name, stock_dict):
                    cart[menu_name] += quantity
                    print_add_cart_msg(menu_name, quantity)
                    break
                else:
                    print_exceed_msg(menu_name, stock_dict)
print_close_store_msg(window_width, income)      
            
                
        
    


    