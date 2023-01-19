phrases = \
{
    'привет': 'здравствуйте', 
    'как тебя зовут?': 'твой компьютер',
    'сколько тебе лет?': 'уже не молод, но еще не стар',
    'как твои дела?': 'отлично',
    'hi': 'Hello! How are you?'
}
is_dialog = True
while is_dialog:
    phrase = input('Я: ').lower()
    if phrase in phrases.keys():
        print(f'Бот: {phrases[phrase]}')
    else:
        print(f'Бот: Я не понимаю')
    if phrase == 'выход':
        is_dialog = False