def main():
    name = ('George', 'Jack', 'Mary')
    age = (10, 23, 17)
    height = (165, 157, 178)
    a = [name, age, height]
    print(sorted(a[1]))
    for i in range(len(a)):
        print("Name=" + a[1][i] + "Age=" + a[2][i] + "Height=" + a[3][i])


main()
