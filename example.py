
def randomGenerator(s, e, a):
    import random
    numbers = []
    for i in range(a):
       
        numbers.append(random.randint(s, e))
    return numbers

#felhasználó által megadott intervallumban generálni felhasználó álltal megadott számot, hány tökéletes szám van az intervallumban osztói összege: szám
def makeNumber(text):
    isCorrect = False
    while not isCorrect:
        n = input(text)
        try:
            n= int(n)
            isCorrect = True
            return n
        except ValueError:
            print("Unexpected value")

###############################################
startMessage = "Startvalue: "

endMessage = "Endvalue: "
amountInput = "Number of numbers: "
start = makeNumber(startMessage) 
stop = makeNumber(endMessage)
amount = makeNumber(amountInput)


print(randomGenerator(start,stop,amount))

