from kiosk.Kiosk import Kiosk

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