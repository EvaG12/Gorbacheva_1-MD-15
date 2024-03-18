day = int(input("dd"))
month = int(input("mm"))
year = int(input("yyyy"))
def magic(day,month,year):
    a = day * month
    yn = year %100
    if a == yn:
        return True
    else:
        return False
print (magic(day,month,year))