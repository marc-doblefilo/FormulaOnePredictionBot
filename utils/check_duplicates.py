from typing import List


def check_duplicates(list: List) -> bool:
    for element in list:
        if list.count(element) > 1:
            return True
    
    return False