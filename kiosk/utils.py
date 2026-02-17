import time

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