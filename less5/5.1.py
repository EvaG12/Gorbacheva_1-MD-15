pn = int(input('введите число'))
def Solve():
    number = [1,3,5,6,8,12]
    if pn in number:
        print (number, "вы угадали число")
    else:
        print(number, "нет такого числа")
print(Solve())