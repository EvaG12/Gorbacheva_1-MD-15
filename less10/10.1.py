def l1():
    import json
    file = 'C:\\python_proj\\1.JSON'
    with open(file, 'r', encoding='utf-8') as file1:
        load = json.load(file1)
        for product in load['products']:
            print(f'Название: {product["name"]}')
            print(f'Цена: {product["price"]}')
            print(f'Вec: {product["weight"]}')
            if product['available']:
                print('В наличии')
            else:
                print('Нет в наличии.')
            print()
        l1()



