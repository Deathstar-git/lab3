def main():
    i = input("Введите кол-во людей: ")
    try:
        int(i)
    except ValueError:
        print("Введено неверное значение!")

    if i.isdigit:
        name = ['Yen', 'Jack', 'Mary']
        name.sort()
        age = [10, 23, 17]
        age.sort()
        height = [165, 196, 180]
        height.sort()
        a = [name, age, height]
        for i in range(len(a)):
            print("Name: " + str(a[0][i]) + " Age: " + str(a[1][i]) + " Height: " + str(a[2][i]))


main()
