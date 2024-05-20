def res():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating = 0):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def res1(self):
            print(f"Название ресторана: {self.restaurant_name}")
            print(f"Тип кухни: {self.cuisine_type}")
            print(f"Рейтинг: {self.rating}")
        def res2(self):
            print(f"Ресторан {self.restaurant_name} открыт!")
        def res3(self, new_rating):
            if 0 <= new_rating <= 5:
                self.rating = new_rating
                print(f"Рейтинг ресторана {self.restaurant_name} обновлен до {self.rating}")
            else:
                print("Рейтинг должен быть в диапазоне от 0 до 5")

    rest1 = Restaurant('Дуо азия', 'Паназиаткая', 4.5)
    rest2 = Restaurant('Il largo', 'Итальянская', 5.0)
    rest3 = Restaurant('Теремок', 'Русская', 4.7)
    rest1.res1()
    rest1.res2()
    print()
    rest2.res1()
    rest2.res2()
    print()
    rest3.res1()
    rest3.res2()
    print()
    rest1.res3(5.0)
    rest1.res1()
res()
