lst = [1, 2, 3, 4, 5, 6]

def modify_list(lst):
    l = []
    for i in lst:
        if i % 2 == 0:
            a = (i // 2)
            l.append(a)
    return l

print (modify_list(lst))
