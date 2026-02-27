def filter_list(l):
    need_filter_list = list(l)
    numbers_only = []
    
    for element in need_filter_list:
        if isinstance(element, (int, float)):
            numbers_only.append(element)
        else:
            pass
    
    return numbers_only
