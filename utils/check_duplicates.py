def check_duplicates(list: list) -> bool:
    for element in list:
        if list.count(element) > 1:
            return True
    
    return False