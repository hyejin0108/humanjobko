from kiosk.Kiosk import Kiosk

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