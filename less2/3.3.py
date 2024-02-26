word = str(input('введите слово'))
s = 0
for f in word:
    if f == "ф" or f == "Ф":
        s +=1
if s != 0:
    print("ого,это редкое слово")
else:
    print('эх, это не очень редкое слово')
