import time

WINDOW_WIDTH = 40
RECEIPT_WIDTH = 30

def digit2str(num : int, digit : int = 3) -> str:
    num = str(num)
    return "0" * (digit-len(num)) + num

def get_current_date_time()->str:
    current_time = time.localtime()
    yyyy = digit2str(current_time.tm_year,4)
    mm = digit2str(current_time.tm_mon,2)
    dd = digit2str(current_time.tm_mday,2)
    hour = digit2str(current_time.tm_hour,2)
    min = digit2str(current_time.tm_min,2)
    sec = digit2str(current_time.tm_sec,2)
    return f"{yyyy}-{mm}-{dd} {hour}:{min}:{sec}"

class Kiosk:
    def __init__(self, name:str):
        self.__store_name = name
        self.__window_width = WINDOW_WIDTH
        self.__receipt_width = RECEIPT_WIDTH
        
        self.__order_number = 0
        self.__income = 0
        self.__stocks = {}
        self.__prices = {}
        self.__menu_names = []
    
        self.__welcome_msg = "어서오세요, %s입니다."
        self.__input_quantity_msg = "> 수량을 입력하세요. "
        self.__exit_cart_msg = "* Enter를 누르면 장바구니로 이동합니다."
        self.__cancel_cart_msg = "* Enter를 누르면 메뉴 추가가 취소됩니다."
        self.__input_menu_msg = "> 주문할 메뉴를 선택하세요. (예시. 1): "
        self.__exceed_stock_msg = "죄송합니다. 현재 %s는 %d만큼 주문가능합니다."
        self.__add_cart_msg = "* 장바구니에 %s %d잔이 추가되었습니다."
        self.__complete_order_msg = "주문이 완료되었습니다."
        self.__complete_sale_msg = "영업이 종료되었습니다."
        
    @property
    def store_name(self):
        return self.__store_name
    
    @store_name.setter
    def store_name(self, store_name:str):
        self.__store_name = store_name
    
    # 주문 print
    def __print_div_line(self):
        print("-"  * self.__window_width)
    
    def __print_welcome_msg(self):
        self.__print_div_line()
        print((self.__welcome_msg%(self.__store_name)).center(self.__window_width))
        self.__print_div_line()
    
    def __print_menu(self):
        print("-"  * self.__window_width)
        print("[Menu]".center(self.__window_width))
        self.__print_div_line()
        for idx, name in enumerate(self.__menu_names):
            print(f"{idx+1}. {name:>10} {self.__prices[name]:>5}원 ({self.__stocks[name]:>3}잔)")
        self.__print_div_line()
    
    def __print_cart_transition_msg(self):
        print(self.__exit_cart_msg)
    
    def __print_cancel_msg(self):
        print(self.__cancel_cart_msg)
        
    def __print_add_cart_msg(self, menu_name:str, quantity:int):
        print(self.__add_cart_msg%(menu_name, quantity))
        
    def __print_exceed_msg(self, menu_name:str):
        print(self.__exceed_stock_msg%(menu_name, self.__stocks[menu_name]))
    
    def __print_complete_order_msg (self):
        print(self.__complete_order_msg)
        
    def __print_close_store_msg(self):
        self.__print_div_line()
        print(self.__complete_sale_msg)
        self.__print_div_line()
        print("영업 매출: " + str(self.__income))    
    
    def __write_receipt(self, cart:dict):
        tot = 0
        for name in cart:
            tot += cart[name] * self.__prices[name]
        # 영수증 메모장에 쓰기
        with open(f"영수증{digit2str(self.__order_number,3)}.txt", mode="w",encoding="utf-8") as f:
            f.write("-" * self.__receipt_width + '\n')
            f.write(self.__store_name.center(self.__receipt_width) + "\n")
            f.write(f"주문 번호 {digit2str(self.__order_number,3)}".center(self.__receipt_width) + "\n")
            f.write("-" * self.__receipt_width + "\n")
            f.write("[주문 내역]".center(self.__receipt_width)+"\n")
            for idx, name in enumerate(cart):
                f.write(f"{idx+1}. {name:>10} {self.__prices[name]:>5}원 ({cart[name]:>3}잔)"+"\n")
            f.write("-" * self.__receipt_width+"\n")
            f.write(f"총 금액: {tot}원"+"\n")
            f.write("-" * self.__receipt_width + "\n")
            f.write(f"주문 일시: {get_current_date_time()}"+"\n")
    
    # 주문 input, bool, function
    def __input_menu(self) -> int:
        menu_number = input(self.__input_menu_msg)
        try:
            if menu_number == "":
                return -1
            elif int(menu_number) > len(self.menu_names):
                print("유효하지 않은 메뉴입니다.")
                return -2
            else:
                return int(menu_number) - 1
        except:
            print("유효하지 않은 메뉴입니다.")
            return -2
        
    def __input_quantity(self) -> int:
        quantity = input(self.__input_quantity_msg)
        try:     
            return -1 if quantity =="" else int(quantity)
        except:
            print("유효하지 않은 메뉴입니다.")
            return -2
    
    def __is_order(self, quantity:int, menu_name:str) -> bool:
        return self.__stocks[menu_name] >= quantity
    
    def __is_all_zero_stock(self) -> bool:
        return sum(self.__stocks.values()) > 0
    
    def __order_complete(self, cart:dict):
        
        for name, quantity in cart.items():
            self.__income += self.__prices[name] * quantity
            self.__stocks[name] -= quantity
    
    def _add_menu(self, menu_name:str, price:int, quantity:int = 0):
        self.__menu_names.append(menu_name)
        self.__prices[menu_name] = price
        self.__stocks[menu_name] = quantity
        
    def _remove_menu(self, menu_name:str):
        self.__menu_names.remove(menu_name)
        del self.__stocks[menu_name]
        del self.__prices[menu_name]
    
    def _add_quantity(self, name:str, quantity:int):
        self.__stocks[name] = quantity
    
    # 주문
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
                    
                    self.__order_complete(cart)
                    
                    self.__print_complete_order_msg()
                    
                    self.__order_number += 1
                    self.__write_receipt(cart)
                    
                    del cart
                    
                    break
                elif menu_number == -2:
                    continue
                else:
                    while True:
                        self.__print_cancel_msg()
                        quantity = self.__input_quantity()
                        if quantity == -1:
                            break
                        elif quantity == -2:
                            continue
                        elif self.__is_order(quantity, menu_name):
                            cart[menu_name] += quantity
                            self.__print_add_cart_msg(menu_name, quantity)
                            break
                        else:
                            self.__print_exceed_msg(menu_name)
        self.__print_close_store_msg()

class StarBucks(Kiosk):
    def __init__(self, branch_name:str, branch_number:int):
        
        self.branch_name = branch_name
        self.branch_number = branch_number
        self.brand_name = "별다방"
        
        store_name = f"{self.brand_name} {self.branch_name} {self.branch_number}호점"
        super().__init__(store_name)
        
        #메뉴
        self._add_menu("Americano", 5000)
        self._add_menu("Latte", 5500)
        self._add_menu("Jucie", 6000)

class BbaekDabang(Kiosk):
    def __init__(self, branch_name:str, branch_number:int):
        
        self.branch_name = branch_name
        self.branch_number = branch_number
        self.brand_name = "빽다방"
        
        store_name = f"{self.brand_name} {self.branch_name} {self.branch_number}호점"
        super().__init__(store_name)
        
        #메뉴
        self._add_menu("Americano", 1500)
        self._add_menu("Latte", 2000)
        self._add_menu("Jucie", 3000)   

#%% main    

starbucks = StarBucks("기흥", 1)
starbucks._add_quantity("Americano", 20)
starbucks._add_quantity("Latte", 10)
starbucks._add_quantity("Jucie", 20)
starbucks.run_store()

    