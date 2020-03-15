# Created by Mateusz Śledź
# Stabilne geny misia

import time
import sys
from random import seed
from random import randint
import statistics
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math

TIME_MEDIAN = 6


def gendata(length):
    seed(randint(0, 4000))
    generated = ''
    for y in range(0, length):
        value = randint(0, 99999)
        value = value % 4
        generated += letters[value]
    return generated


def prepare():
    amountC = genome.count("C")
    amountA = genome.count("A")
    amountT = genome.count("T")
    amountG = genome.count("G")

    if choice != 3:
        print(genome)
        print("C: " + str(amountC))
        print("A: " + str(amountA))
        print("T: " + str(amountT))
        print("G: " + str(amountG))

    goodAmount = int(length / 4)
    amountA -= goodAmount
    amountC -= goodAmount
    amountT -= goodAmount
    amountG -= goodAmount

    shortestPossible = 0
    whichToDel = []
    toDel = {}
    toAdd = {}
    saved_letters = {}
    amounts = [amountC, amountA, amountT, amountG]

    i = 0
    for value in amounts:
        if i == 0:
            letter = 'C'
        elif i == 1:
            letter = 'A'
        elif i == 2:
            letter = 'T'
        elif i == 3:
            letter = 'G'
        if value > 0:
            whichToDel.append(letter)
            toDel[letter] = value
            shortestPossible += value
        else:
            toAdd[letter] = -1 * value
        i += 1

    for y in whichToDel:
        saved_letters[y] = 0

    return shortestPossible, whichToDel, toDel, toAdd, saved_letters


def showtable():
    temp3 = []
    n_median = int(len(temp1)/2)

    c = ((math.log(temp1[n_median])*temp1[n_median])/temp2[n_median])

    for y in range(0, len(temp1)):
        temp3.append(c*temp2[y]/(math.log(temp1[y])*temp1[y]))

    t.add_column('q(n)', temp3)
    print(t)

    plt.plot(temp1, temp2)
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.title('Complexity')
    plt.show()

    plt.hist(temp3)
    plt.title('q(n) values')
    plt.ylabel('Number of occurences')
    plt.show()


def showresult():
    print("Best result is: " + result)
    print("Lenght of result: " + str(len(result)))

    print("Result contains:   C: " + str(result.count("C")) + "  A: " + str(result.count("A")) + " T: " + str(
        result.count("T")) + " G: " + str(result.count("G")))

    print("\nReplacing contains: ")

    for letter in toAdd:
        print(letter + " : " + str(result.count(letter) + toAdd.get(letter)))

    for letter in toDel:
        print(letter + " : " + str(result.count(letter) - toDel.get(letter)))        


print("Choose option: ")
print("1. Generate genome automatically...")
print("2. Put your own genome (length dividable by 4)")
print("3. Generate genome and measure time")

choice = int(input("Choice: "))

genome = ''

if choice == 3:
    n = int(input("Number of iterations: "))
    length = int(input('Initial length: '))
    plusLen = int(input('Each iteration bigger: '))
    counter = 0
    n = TIME_MEDIAN * n
    temp1 = []
    temp2 = []
    temp4 = []

elif choice == 1:
    length = int(input("Enter length of genome (dividable by 4): "))
    n = 1
    counter = 0
    if length % 4 is not 0:
        sys.exit()

elif choice == 2:
    genome = input("Enter genome - only letters A, C, T, G. Length of your word must be dividable by 4: ")
    length = len(genome)
    n = 1
    counter = 0
    if length % 4 is not 0:
        sys.exit()
else:
    sys.exit()


for s in range(0, n):

    letters = ['C', 'A', 'T', 'G']

    if counter == TIME_MEDIAN:
        length += plusLen
        counter = 1
    elif choice == 3:
        counter += 1

    if choice != 2:
        genome = gendata(length)

    shortestPossible, whichToDel, toDel, toAdd, saved_letters = prepare()

    if shortestPossible == 0:
        print('Your genome is already stable :)')
        sys.exit()

    if choice != 3:
        print("shortest possible: " + str(shortestPossible))
        print("Too much of: " + str(toDel))

    currLen = shortestPossible
    f = 0
    result = ''
    first = 0
    jumplen = int(shortestPossible / 10)

    if jumplen == 0:
        jumplen += 1

    if choice == 3:
        start = time.time()

    while currLen != length:
        #print(currLen)      #uncomment this to better see how algorithm works

        temp = genome[0: currLen]
        for p in whichToDel:
            saved_letters[p] = temp.count(p)

        for x in range(0, length - currLen + 1):
            temp = genome[x: x + currLen]
            if x != 0:
                addlast = temp[-1:]
                if addlast in saved_letters:
                    saved_letters[addlast] += 1

            for p in whichToDel:
                if saved_letters.get(p) >= toDel.get(p):
                    f += 1
                else:
                    delfirst = temp[0: 1]
                    if delfirst in saved_letters:
                        saved_letters[delfirst] -= 1
                    f = 0
                    break
            if f is len(whichToDel):
                if first == 0:
                    if shortestPossible == currLen:
                        first = 1
                        result = temp
                        break
                    first = 1
                    currLen -= jumplen
                    f = 0
                    break
                elif first == 1:
                    result = temp
                    break
        if first == 0:
            currLen += jumplen
        elif first == 1:
            if result != '':
                break
            else:
                currLen += 1

    if choice == 3:
        end = time.time()
        t = PrettyTable()
        fin = end - start
        temp4.append(fin)
        if counter == TIME_MEDIAN:
            temp1.append(length)
            temp2.append(statistics.mean(temp4))
            temp4.clear()

        t.add_column('n', temp1)
        t.add_column('T(n) [s]', temp2)

    else:
        showresult()

if choice == 3:
    showtable()
