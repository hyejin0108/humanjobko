welcome_msg = "어서오세요, %s입니다."
input_quantity_msg = "> 수량을 입력하세요. "
exit_cart_msg = "* Enter를 누르면 장바구니로 이동합니다."
cancel_cart_msg = "* Enter를 누르면 메뉴 추가가 취소됩니다."
input_menu_msg = "> 주문할 메뉴를 선택하세요. (예시. 1): "
exceed_stock_msg = "죄송합니다. 현재 %s는 %d만큼 주문가능합니다."
add_cart_msg = "* 장바구니에 %s %d잔이 추가되었습니다."
complete_order_msg = "주문이 완료되었습니다."
complete_sale_msg = "영업이 종료되었습니다."

WINDOW_WIDTH = 40

class Kiosk:
    def __init__(self, name):
        self.__window_width = WINDOW_WIDTH
        self.__store_name = name
        self.__income = 0
        self.__stocks = {}
        self.__prices = {}
        self.__menu_names = []
        
    
    def __print_div_line(self):
        print("-"  * self.__window_width)
    
    def __print_welcome_msg(self):
        self.__print_div_line()
        print((welcome_msg%(self.__store_name)).center(self.__window_width))
        self.__print_div_line()
    
    def __print_menu(self):
        print("-"  * self.__window_width)
        print("[Menu]".center(self.__window_width))
        self.__print_div_line()
        for idx, name in enumerate(self.__menu_names):
            print(f"{idx+1}. {name:>10} {self.__prices[name]:>5}원 ({self.__stocks[name]:>3}잔)")
        self.__print_div_line()
    
    def __print_cart_transition_msg(self):
        print(exit_cart_msg)
    
    def __print_cancel_msg(self):
        print(cancel_cart_msg)
        
    def __print_add_cart_msg(self, menu_name, quantity):
        print(add_cart_msg%(menu_name, quantity))
        
    def __print_exceed_msg(self, menu_name):
        print(exceed_stock_msg%(menu_name, self.__stocks[menu_name]))
    
    def __print_complete_order_msg (self):
        print(complete_order_msg)
        
    def __print_close_store_msg(self):
        self.__print_div_line()
        print(complete_sale_msg)
        self.__print_div_line()
        print("영업 매출: " + str(self.__income))
        
    def __input_menu(self):
        menu_number = input(input_menu_msg)
        if menu_number == "":
            return -1
        else:
            return int(menu_number) - 1
        
    def __input_quantity(self):
        quantity = input(input_quantity_msg)
        if quantity == "":
            return -1
        else:
            return int(quantity)
        
    def __is_order(self, quantity, menu_name):
        return self.__stocks[menu_name] >= quantity
    
    def __is_all_zero_stock(self):
        return sum(self.__stocks.values()) > 0
    
    def _add_menu(self, menu_name, price, quantity):
        self.__menu_names.append(menu_name)
        self.__prices[menu_name] = price
        self.__stocks[menu_name] = quantity
        
    def _remove_menu(self, menu_name):
        self.__menu_names.remove(menu_name)
        del self.__stocks[menu_name]
        del self.__prices[menu_name]
    
    def _add_quantity(self, name, quantity):
        self.__stocks[name] = quantity
    
    def run_store(self):
        while self.__is_all_zero_stock():
            self.__print_welcome_msg()
            self.__print_menu()
            
            cart = {name : 0 for name in self.__menu_names}
            
            while True:
                self.__print_cart_transition_msg()
                menu_number = self.__input_menu()
                menu_name = self.__menu_names[menu_number]
            
                if menu_number == -1: # 주문 완료
                
                    for name, quantity in cart.items():
                        self.__income += self.__prices[name] * quantity
                        self.__stocks[name] -= quantity
                        
                    del cart
                    
                    self.__print_complete_order_msg()
                    break
                else:
                    while True:
                        self.__print_cancel_msg()
                        quantity = self.__input_quantity()
                        if quantity == -1:
                            break
                        elif self.__is_order(quantity, menu_name):
                            cart[menu_name] += quantity
                            self.__print_add_cart_msg(menu_name, quantity)
                            break
                        else:
                            self.__print_exceed_msg(menu_name)
        self.__print_close_store_msg()

class StarBucks(Kiosk):
    def __init__(self, branch_name, branch_number, width):
        #메뉴
        self._add_menu("Americano", 5000,0)
        self._add_menu("Latte", 5500,0)
        self._add_menu("Jucie", 6000,0)
        #
        self.branch_name = branch_name
        self.branch_number = branch_number
        self.brand_name = "별다방"
        
        store_name = f"{self.brand_name} {self.branch_name} {self.branch_number}호점"
        super().__init__(width, store_name)

class BbaekDabang(Kiosk):
    def __init__(self, branch_name, branch_number, width):
        #메뉴
        self._add_menu("Americano", 1500,0)
        self._add_menu("Latte", 2000,0)
        self._add_menu("Jucie", 3000,0)
        #
        self.branch_name = branch_name
        self.branch_number = branch_number
        self.brand_name = "빽다방"
        
        store_name = f"{self.brand_name} {self.branch_name} {self.branch_number}호점"
        super().__init__(width, store_name)
    

#%% main    
starbucks = StarBucks("기흥", "1", 40)
starbucks._add_quantity("Americano", 20)
starbucks._add_quantity("Latte", 10)
starbucks._add_quantity("Jucie", 20)
starbucks.run_store()

bbaek = BbaekDabang("상갈", "2", 40)
bbaek._add_quantity("Americano", 20)
bbaek._add_quantity("Latte", 10)
bbaek._add_quantity("Jucie", 20)
bbaek.run_store()

    