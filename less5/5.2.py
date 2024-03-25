def a():

    number = [1,4,5,4,6,9,10,0]
    l = []
    for i in number:
        if number.count(i)>1 and i not in l:
            l.append(i)
        if len(l)>0:
            print(l[0])
        else:
            print("повторов нет")
