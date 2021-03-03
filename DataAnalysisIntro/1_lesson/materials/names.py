# Файл more_names.py

# Объявляем глобальную переменную name для применения во всех функциях
name = str(input('Your name: '))

# Определяем функцию, чтобы проверить, содержит ли имя гласную букву
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Has Vowel!')
    else:
        print('There is no Vowel! :(')
def welcome():
    print('Welcome!')

# Выполняем функцию main()
if __name__ == '__main__':
    has_vowel()
    
welcome()