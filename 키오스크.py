class Kiosk:
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
    
    window_width = 0
    income = 0
    store_name = ""
    stocks = {}
    prices = {}
    menu_names = []
    
    def __init__(self, width, name):
        self.window_width = width
        self.store_name = name
    
    def print_div_line(self):
        print("-"  * self.window_width)
    
    def print_welcome_msg(self):
        self.print_div_line()
        print((self.welcome_msg%(self.store_name)).center(self.window_width-len(self.store_name)-8))
        self.print_div_line()
    
    def print_menu(self):
        print("-"  * self.window_width)
        print("[Menu]".center(self.window_width))
        self.print_div_line()
        for idx, name in enumerate(self.menu_names):
            print(f"{idx+1}. {name:>10} {self.prices[name]:>5}원 ({self.stocks[name]:>3}잔)")
        self.print_div_line()
    
    def print_cart_transition_msg(self):
        print(self.exit_cart_msg)
    
    def print_cancel_msg(self):
        print(self.cancel_cart_msg)
        
    def print_add_cart_msg(self, menu_name, quantity):
        print(self.add_cart_msg%(menu_name, quantity))
        
    def print_exceed_msg(self, menu_name):
        print(self.exceed_stock_msg%(menu_name, self.stocks[menu_name]))
    
    def print_complete_order_msg (self):
        print(self.complete_order_msg)
        
    def print_close_store_msg(self):
        self.print_div_line()
        print(self.complete_sale_msg)
        self.print_div_line()
        print("영업 매출: " + str(self.income))
        
    def input_menu(self):
        menu_number = input(self.input_menu_msg)
        if menu_number == "":
            return -1
        else:
            return int(menu_number) - 1
        
    def input_quantity(self):
        quantity = input(self.input_quantity_msg)
        if quantity == "":
            return -1
        else:
            return int(quantity)
        
    def is_order(self, quantity, menu_name):
        return self.stocks[menu_name] >= quantity
    
    def is_all_zero_stock(self):
        return sum(self.stocks.values()) > 0
    
    def add_menu(self, menu_name, price, quantity):
        self.menu_names.append(menu_name)
        self.prices[menu_name] = price
        self.stocks[menu_name] = quantity
        
    def remove_menu(self, menu_name):
        self.menu_names.remove(menu_name)
        del self.stocks[menu_name]
        del self.prices[menu_name]
    
    def run_store(self):
        while self.is_all_zero_stock():
            self.print_welcome_msg()
            self.print_menu()
            
            cart = {name : 0 for name in self.menu_names}
            
            while True:
                self.print_cart_transition_msg()
                menu_number = self.input_menu()
                menu_name = self.menu_names[menu_number]
            
                if menu_number == -1: # 주문 완료
                
                    for name, quantity in cart.items():
                        self.income += self.prices[name] * quantity
                        self.stocks[name] -= quantity
                        
                    del cart
                    
                    self.print_complete_order_msg()
                    break
                else:
                    while True:
                        self.print_cancel_msg()
                        quantity = self.input_quantity()
                        if quantity == -1:
                            break
                        elif self.is_order(quantity, menu_name):
                            cart[menu_name] += quantity
                            self.print_add_cart_msg(menu_name, quantity)
                            break
                        else:
                            self.print_exceed_msg(menu_name)
        self.print_close_store_msg()

#%% main    
starbucks = Kiosk(40, "별다방")
starbucks.add_menu("Americano", 5000,10)
starbucks.add_menu("Latte", 5500,7)
starbucks.add_menu("Jucie", 6000, 4)
starbucks.run_store()   

starbucks = Kiosk(40, "백다방")
starbucks.add_menu("Americano", 1000,10)
starbucks.add_menu("Latte", 2000,7)
starbucks.add_menu("Jucie", 3000, 4)
starbucks.run_store()

    