def main():
    name = ('Yen', 'Jack', 'Mary')
    age = (10, 23, 17)
    height = (165, 157, 178)
    a = [name, age, height]
    sorted(a)
    for i in range(len(a)):
        print("Name:" + str(a[0][i]) + " Age:" + str(a[1][i]) + " Height:" + str(a[2][i]))


main()
