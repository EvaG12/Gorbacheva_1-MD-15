
strana = str(input("введите страну"))
slovar = {"Россия" : "Москва","Великобритания" : "Лондон", "Япония" : "Токио"}
def slovari():
    st1 = " "
    a = slovar.items()
    if strana == "Россия":
        st1 = slovar.get("Россия")
    if strana == "Великобритания":
        st1 = slovar.get("Великобритания")
    if strana == "Япония":
        st1 = slovar.get("Япония")
    sslovar = sorted(slovar.items())
    print(a, st1, sslovar)
print(slovari())
