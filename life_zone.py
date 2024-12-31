#импортируем библиотеку
import math 
qwe = lambda L1,L2: math.sqrt(L1/L2) #пишем формулу


def main():
    L1 = float(input('Показатель звезды:'))
    L2 = float(input('Показатель солнца:'))
    print('Средний радиус:', qwe(L1,L2)) #вывод

    

if __name__ == "__main__":
        main()