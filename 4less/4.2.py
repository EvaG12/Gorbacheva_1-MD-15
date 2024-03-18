a = int(input("введите число"))
def delen():
    return 100/a
try:
    print (delen())
except ZeroDivisionError:
    print ('делить на ноль нельзя')


