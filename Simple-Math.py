import re

class inputnum():
    def inputnum1():
        input1 = input("Type a number followed by +, -, * or / followed by another number:  ")
        input1 = re.split('(\d+)', input1)
        while '' in input1:
            input1.remove('')
        a = int(input1[0])
        b = input1[1]
        c = int(input1[2])
        return(a, b, c)

class mathadd1():
    def mathadd(a, b, c):
        if b == "+":
            result = a + c
            return(result)

class mathsubtract1():
    def subtract(a, b, c):
        if b == "-":
            result = a - c
            return(result)
class mathmultiply1():
    def mathmultiply(a, b, c):
        if b == "*":
            result = a * c
            return(result)

class mathdivide1():
    def mathdivide(a, b, c):
        if b == "/":
            result = a / c
            return(result)

class printResult():
    def printRes(a, b, c, result):
        print(a, b, c, "=", result)

class checkOperator():
    def checkOp(a, b, c):
        if b == "+":
            result = mathadd1.mathadd(a, b, c)
        elif (b == "-"):
            result = mathsubtract1.subtract(a, b, c)
        elif (b == "*"):
            result = mathmultiply1.mathmultiply(a, b, c)
        elif (b == "/"):
            result = mathdivide1.mathdivide(a, b, c)
        printResult.printRes(a, b, c, result)


a, b, c = inputnum.inputnum1()
checkOperator.checkOp(a, b, c)
