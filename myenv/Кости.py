import random
import time

try:
    def game():
        a = input("Брось два кубика чтобы узнать результат. Для броска кубиков нажми клавишу Enter")
        f_kub = random.randint(1, 6)
        s_kub = random.randint(1, 6)
        total = f_kub + s_kub
        print("Loading...")
        time.sleep(0.8)
        print(f"Результат броска: {f_kub} - {s_kub}. Итоговая сумма чисел = {total}")

    game()

    def game_2():
        print("")
        b = int(input("Бросить еще раз? 1 - да, 2 - нет "))
        while b ==1:
            game()
            print("")
            b = int(input("Бросить еще раз? 1 - да, 2 - нет "))
        else:
            print("Выход из игры")

    game_2()

except ValueError:
    print("Нужно ввести число 1 или 2")
    game_2()

