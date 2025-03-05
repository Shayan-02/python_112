def separator(ls):
    lst1 = []
    lst2 = []
    for _ in ls:
        if _ % 2 == 0:
            lst1.append(_)
        else:
            lst2.append(_)
    print((lst1, lst2))


lst = [int(_) for _ in input().split()]
separator(lst)