import statistics

def valid_check():
    try:
        return float(input("Give me a number: "))
    except ValueError:
        print("That is not a number, please try again.")

def valid_loop():
    inp = valid_check()
    while inp is None:
        inp = valid_check()
    else:
        return inp

def isPos(a):
    while a < 0:
        print("List sizes are positive. Your number was negative, please try again.")
        a = valid_loop()
    else:
        return a

def listBuilder(a):
    print("Now we will build the list.")
    new_list = []
    while a:
        new_list.append(valid_loop())
        a -= 1
    return new_list

def listSum(a):
    return sum(a)

def avg(a):
    return statistics.mean(a)

def main():
    print('''
This program allows you to build a list and determine its size.
Please enter a positive number for the size of list you want.''')
    vl = valid_loop()
    posCheck = isPos(vl)
    completeList = listBuilder(posCheck)
    print("Here is your list:\n" + str(completeList))
    print("The sum of the list is: {0}".format(round(listSum(completeList),2)))
    print("The average of the list is: {0}".format(round(avg(completeList),2)))
    return

main()