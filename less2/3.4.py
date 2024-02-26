import random
otv = 0
ohs = 0
while ohs != 3:
    a = random.randrange(0,10)
    b = random.randrange(0, 10)
    c = a + b
    prim = str(a) + "+" + str(b) + "="
    print (prim, end=" ")
    po = int(input(" "))
    if po == c:
        otv +=1
        print("right")
    else:
        ohs +=1
        print("wrong")
print ("игра oкончена. правильных ответов:" , otv)
