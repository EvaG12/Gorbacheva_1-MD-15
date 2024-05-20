def l3():
    with open('C:\\python_proj\\rus_eng.txt', 'r', encoding='utf-8') as f:
        rows = f.readlines()
    rus_eng = {}
    for row in rows:
        words = row.strip().split(' - ')
        if len(words) == 2:
            eng = words[0]
            rus_words = words[1].split(', ')
            for word in rus_words:
                rus_eng[word] = en
    sort = dict(sorted(rus_eng.items()))
    with open('C:\\python_proj\\ru-en.txt', 'w', encoding='utf-8') as file:
        for rus, eng in sort.items():
            file.write(f'{rus} - {eng}\n')
l3()