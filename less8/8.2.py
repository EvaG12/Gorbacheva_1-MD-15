from PIL import Image
def otkr():
    cards = {"др":'Z:\\1-МД-15\\Горбачева Ева Артуровна\\birthday.jpg', "9 мая": 'Z:\\1-МД-15\\Горбачева Ева Артуровна\\may9.jpg' ,"8 марта":'Z:\\1-МД-15\\Горбачева Ева Артуровна\\march9 .jpg' }
    hol = str(input("введите праздник"))
    if hol in cards:
        c = cards[hol]
        if c:
            i = Image.open(c)
            i.show()
        else:
            print("-")
    else:
        print("--")
print(otkr())
