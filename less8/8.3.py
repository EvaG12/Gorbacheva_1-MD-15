from PIL import Image, ImageDraw, ImageFont
def congrats():
    name = str(input("name?"))
    i = Image.open('Z:\\1-МД-15\\Горбачева Ева Артуровна\\otkritka.jpg')
    a = ImageFont.truetype("arial.ttf", 30)
    b = ImageDraw.Draw(i)
    b.text((400,10), f'{name} congratulations!', font=a, fill = "red")
    i.show()
    i.save('Z:\\1-МД-15\\Горбачева Ева Артуровна\\otkritka2.jpg')
print(congrats())
