def l2():
    import json
    file = 'C:\\python_proj\\1.JSON'
    name = input('Введите название продукта: ')
    price = float(input('Введите цену продукта: '))
    weight = float(input('Введите вес продукта: '))
    available = input('Продукт доступен? (да/нет): ').strip().lower() == 'да'
    with open(file, 'r', encoding='utf-8') as file1:
        load = json.load(file1)
    n_p = {'name': name,
           'price': price,
           'weight': weight,
           'available': available}
    load['products'].append(n_p)
    with open(file, 'w', encoding='utf-8') as file1:
        json.dump(load, file1, ensure_ascii=False, indent=4)
    print('\nНовый список:')
    for product in load['products']:
        print(f'Название: {product["name"]}')
        print(f'Цена: {product["price"]}')
        print(f'Вec: {product["weight"]}')
        if product['available']:
            print('В наличии')
        else:
            print('Нет в наличии.')
        print()
    l2()

