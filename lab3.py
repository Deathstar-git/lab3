import argparse


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument('i', type=int)

    return p


def main(i):
    choose_sort = {0: 'Сортировка по имени:', 1: 'Сортировка по росту:', 2: 'Сортировка по возрасту:'}
    print(str(choose_sort[i]))
    lst = [('Vanya', 172.5, 17), ('Petya', 186.0, 20), ('Anya', 168.3, 16),
           ('Masha', 178.7, 19), ('Oleg', 168.3, 17), ('Kolya', 180.4, 18), ('Natasha', 175.0, 20),
           ('Boris', 159.8, 16), ('Galina', 157.3, 18), ('Maks', 177.0, 19)]
    lst = sorted(lst, key=lambda tpl: tpl[i])
    for j in range(len(lst)):
        print(lst[j])
    sum_r = 0
    sr = 0
    for j in range(len(lst)):
        sum_r = sum_r + float(lst[j][1])
        sr = sum_r/(len(lst))
    sr = float('{:.2f}'.format(sr))
    print('Cредний рост:' + str(sr))
    sum_v = 0
    sv = 0
    for j in range(len(lst)):
        sum_v = sum_v + int(lst[j][2])
        sv = sum_v/(len(lst))
    print('Cредний возраст:' + str(sv))

    lst_srt_v = sorted(lst, key=lambda tpl: tpl[2])
    mv = lst_srt_v[int(len(lst)/2)][2]
    print('Медианный возраст равен:' + str(mv))

    lst_srt_r = sorted(lst, key=lambda tpl: tpl[1])
    mr = lst_srt_r[int(len(lst)/2)][1]
    print('Медианный рост равен:' + str(mr))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    main(namespace.i)
