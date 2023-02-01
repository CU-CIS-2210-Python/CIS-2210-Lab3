def myFunction(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return 3 * num + 1

def getAge():
    val = input("How old are you? ")
    return int(val)

age = getAge()

someNumber = myFunction(age)

print('Your lucky number is ' + str(someNumber))


