import random

number = input('Количество паролей:')
length = input('Длина пароля:')
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int(number)
length = int(length)

for n in  range (number):
    password = ''
    for i in range(length):
        password+= random.choice(chars)
    print(password)

