def isitPerfect(n):
    if n ==1 or n ==0:
        return False
    else: 
        divNumbers = [1]
        for i in range(2,n):
                if n % i == 0:
                    divNumbers.append(i)
                    return sum(divNumbers) == n







def randomGenerator(s, e, a):
    import random
    numbers = []
    for i in range(a):
       
        numbers.append(random.randint(s, e))
    return numbers

#felhasználó által megadott intervallumban generálni felhasználó álltal megadott számot, hány tökéletes szám van az intervallumban osztói összege: szám
def makeNumber(text):
    #isCorrect = False
    while True: #not isCorrect:
        n = input(text)
        try:
            n= int(n)
            #isCorrect = True
            return n
        except ValueError:
            print("Unexpected value")

###############################################
#main
startMessage = "Startvalue: "

endMessage = "Endvalue: "
amountInput = "Number of numbers: "
start = makeNumber(startMessage) 
stop = makeNumber(endMessage)
amount = makeNumber(amountInput)

perfectNumfreq = {}
perfectNumList = []
randomNumbers = randomGenerator(start,stop,amount)
for num in randomNumbers:
    if isitPerfect(num):
        perfectNumList.append(num)



 ###       
for i in perfectNumList:
    if i in perfectNumfreq.keys():
        perfectNumfreq[num] +=1
    else: 
        perfectNumfreq[num] = 1

for key in perfectNumfreq.keys():
    print(f"{key}: {perfectNumList}")