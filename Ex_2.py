file = open('fruits.txt', encoding='utf-8')
fruits = file.readline().split(' ')
file.close()
letter = input('Введите букву ')
for fruit in fruits:
    if fruit[0].lower() == letter.lower():
        print(fruit)