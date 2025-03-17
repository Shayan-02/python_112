def listReverse(ls):
    for _ in ls[::-1]:
        print(_)


lst = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        lst.append(a)

listReverse(lst)
