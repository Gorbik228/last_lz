import pyramid as p
import life_zone as l


def main():
    user = int(input("Выберите функцию 1 или 2: "))
    if user == 1:
        S1 = float(input('Площадь верхнего основания:'))
        S2 = float(input('Площадь нижнего основания:'))
        H  = float(input('Высота усеченной пирамиды:'))
        print('Объем усеченной пирамиды  :', (p.qwe(S1,S2,H))) #вывод
    elif user == 2:
        L1 = float(input('Показатель звезды:'))
        L2 = float(input('Показатель солнца:'))
        print('Средний радиус:', l.qwe(L1,L2)) #вывод
        
    else:
            print('выберите 1 или 2')



if __name__ == "__main__":
    main()