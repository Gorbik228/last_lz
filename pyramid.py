#импортируем библиотеку
import math

qwe = lambda S1,S2,H: (H/3*(S1 + S2 + math.sqrt(S1*S2))) #пишем формулу

def main():
    S1 = float(input('Площадь верхнего основания:'))
    S2 = float(input('Площадь нижнего основания:'))
    H  = float(input('Высота усеченной пирамиды:'))
    print('Объем усеченной пирамиды  :', (qwe(S1,S2,H))) #вывод


if __name__ == "__main__":
            main()