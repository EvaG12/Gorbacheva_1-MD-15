from PIL import Image
def otkr():
    i = Image.open('Z:\\1-МД-15\\Горбачева Ева Артуровна\\otkritka.jpg')
    i2 = i.crop((0,20,1000,700))
    i2.save('Z:\\1-МД-15\\Горбачева Ева Артуровна\\otkritka1.jpg')
    i2.show()
print(otkr())


