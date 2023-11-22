import logging
from random import randint as ri 

logging.basicConfig(filename='try_game.log', level=logging.INFO)

N = int(input("Введите границу загаданного числа:"))
logging.info(f"Загадано число от 1 до {N}")

k = int(input("Введите количество попыток:"))
logging.info(f"Количество попыток равно {k}")

x, p = ri(1, N), 1
logging.info(f"Загаданно число равно {x}")

tryy = int(input(f"Введите число от 1 до {N}:"))
logging.info(f"Пользователь ввел число {tryy}")

if (tryy > N) or (tryy < 1):
    print("Вы ввели неправильное число!")
    tryy = int(input(f"Введите число от 1 до {N}:"))
    logging.info(f"Пользователь ввел число {tryy}")
    logging.info(f"Программа вывела 'Вы ввели неправильное число!'")

while tryy != x: 
    if p == k: 
        print("Попытки закончились! Загаданное число было:", x) 
        logging.info(f"Программа вывела 'Попытки закончились! Загаданное число было: {x}'")
        exit() 
    p += 1; 
    print("Попробуйте ещё раз!")
    if tryy > x:
        print("Загаданное число меньше") 
        tryy = int(input("Введите число:"))
        logging.info(f"Пользователь ввел число {tryy}")
        if (tryy > N) or (tryy < 1):
            print("Вы ввели неправильное число!")
            tryy = int(input(f"Введите число от 1 до {N}:"))
            logging.info(f"Пользователь ввел число {tryy}")
            logging.info(f"Программа вывела 'Вы ввели неправильное число!'")
    if tryy < x:
        print("Загаданное число больше")
        tryy = int(input("Введите число:"))
        logging.info(f"Пользователь ввел число {tryy}")
        if (tryy > N) or (tryy < 1):
            print("Вы ввели неправильное число!")
            tryy = int(input(f"Введите число от 1 до {N}:"))
            logging.info(f"Пользователь ввел число {tryy}")
            logging.info(f"Программа вывела 'Вы ввели неправильное число!'")

print("Вы угадали!")
logging.info(f"Программа вывела 'Вы угадали!'")