count = int(input('Введите число '))
first = 0
second = 1
file = open('result.txt', mode='w', encoding='utf-8')
for i in range(count):
    file.write(str(first) + '\n')
    current = first
    first = second
    second = current + second
file.close()