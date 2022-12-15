def passw(a):
    b = a.casefold()
    num = 0
    for i in b:
        if i.isdigit():
            num += 1
    if num == 0:
        print('False')
        print('Ваш пароль не подходит по условиям, пароль должен содержать цифры')
    elif 'password' in b :
        print("False")
        print('Ваш пароль не подходит по условиям,попробуйте не использовать слова типа : password')
    elif len(b) <= 6 :
        print("False")
        print('Ваш пароль не подходит по условиям, пароль должен быть длиннее 6 символов')
    elif b.isnumeric() == True :
        print('False')
        print('Ваш пароль не подходит по условиям, пароль не должен состоять только из цифр')
    else:
        print('True')
        print('Ваш пароль успешно установлен')
k = passw(str(input('Введите, пожалуйста, ваш пароль : ')))
