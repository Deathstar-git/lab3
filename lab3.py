
def main():
    height_true = True
    age_true = True
    name_true = True
    name = ('Misha', 'Petya', 'Natasha', 'Vanya', 'Darya', 'Lena', 'Fedya', 'Zina', 'Alesha', 'Vlad')
    name = sorted(name, reverse=name_true)
    height = (178.2, 167.5, 183.6, 172.0, 159.1, 164.7, 170.5, 175.3, 189.2, 196.0)
    height = sorted(height, reverse=height_true)
    age = (17, 18, 20, 17, 17, 19, 18, 19, 20, 19)
    age = sorted(age, reverse=age_true)
    a = [name, height, age]
    for i in range(len(name)):
        print("Name: " + str(a[0][i]) + ", Height: " + str(a[1][i]) + ", Age: " + str(a[2][i]))


main()
