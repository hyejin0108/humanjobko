from kiosk.kiosk_starbucks import StarBucks

if __name__ == "__main__":
    starbucks = StarBucks("기흥", 1)
    starbucks._add_quantity("Americano", 20)
    starbucks._add_quantity("Latte", 10)
    starbucks._add_quantity("Jucie", 20)
    starbucks.run_store()