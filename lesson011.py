if __name__ == '__main__':
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    print('-'*50)

    for i in range(len(fruits)):
        print(i, fruits[i])
    print('-'*50)

    for i, fruit  in enumerate(fruits):
        print(i, fruits[i])
    print('-'*50)




