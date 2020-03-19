import webbrowser
import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

from pythonds.basic.stack import Stack
import string
import math
import numpy

def is_float(input):
  try:
    num = float(input)
  except ValueError:
    return False
  return True

def tempmath(mystring):
 count = 0
 flag = 0
 question = mystring
 print(question)
 f = open('db/x.txt','r')
 line = f.readline()
 while line:
     thisline = line.split(" ")                  # Classification
     for x in range(1,len(thisline)):
         check = thisline[x] in question
         if check == True:
             count = count + 1
             flag = 1                            # Abort Sequence
     if count == len(thisline) - 2:
         print(thisline[0])
         nextdb = thisline[0]
     count = 0
     line = f.readline()
 if flag == 0:
   return "Error"
 f.close()

 flag = 0
 count = 0
 question2 = question.split(" ")              # User String
 f2 = open("db/"+nextdb,'r')
 line2 = f2.readline()
 while line2:
     thisline2 = line2.split(" ")             # next database's strings
     for x2,xq in zip(thisline2, question2):
         if x2 == xq:
             count = count + 1
         elif x2 == ':':
             break
         else:
             f3 = open('bin/tokens.txt','r')
             varline = f3.readline()         # variable list
             if x2 in varline:
                 count = count + 1        
 #    print(count)
     if count == len(question2):
         print("Classification Passed")
         flag = 1
         break
     count = 0
     line2 = f2.readline()
 if flag == 0:
   return "Error"
 count = 0
 #print(thisline2)
 f4 = open('temp/tempvar.txt','w')
 f4cop = open('temp/tempval.txt','w')
 for x3 in thisline2:
     if x3 == ':':
         break
     else:
         if x3 in varline:
 #            print(count)
             f4.write(x3+" "+question2[count]+" ~\n")
             f4cop.write(question2[count]+" ")
     count = count + 1
 f4cop.write(" ~\n")
 f4cop.close()
 f4.close() 
 f3.close()

 f5 = open('temp/tempmath.txt','w')
 colonindex = (thisline2.index(':'))
 for xnum in range (colonindex+1,len(thisline2)):
     f5.write(thisline2[xnum]+" ")
 f5.close()
 f2.close()
 newstr = mathcalc()
 return newstr

def mathcalc():
 f1 = open('temp/tempvar.txt','r')
 f2 = open('temp/tempmath.txt','r')
 mymath = f2.readline()
 #print(mymath)
 #print(infixToPostfix(mymath))
 f3 = open('temp/tempmathpf.txt','w')
 f3.write(infixToPostfix(mymath)+"\n")
 f3.close()
 f2.close()

 fpf = open('temp/tempmathpf.txt','r')
 postnot = fpf.readline()
 #print(postnot)
 line = f1.readline()
 while line:
     thisline = line.split()
     if thisline[0] in postnot:
         postnot = postnot.replace(thisline[0], thisline[1])
         #print(postnot)
     line = f1.readline()
 f4 = open('temp/tempmathpfnum.txt','w')
 f4.write(postnot+"\n")
 f4.close()
 fpf.close()
 f1.close()
 newstr = mathsolve()
 return newstr
 
def mathsolve():
    f1 = open('temp/tempmathpfnum.txt','r')
    solving = f1.readline()
    newstr = postfixEval(solving)
    f1.close()
    return newstr
    
def infixToPostfix(infixexpr):
    ftok = open('bin/tokens.txt','r')
    tok = ftok.readline()
    prec = {}
    prec["sin"] = 3
    prec["cos"] = 3
    prec["tan"] = 3
    prec["sinr"] = 3
    prec["cosr"] = 3
    prec["tanr"] = 3
    prec["^"] = 3
    prec["sqrt"] = 3
    prec["%"] = 3
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    #print(tokenList)
    for token in tokenList:
        if token in tok or is_float(token):
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
    ftok.close()
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixExpr):
    print(postfixExpr)
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if is_float(token):
            operandStack.push(float(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        if op2 == 0:
          return "Infinity"
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "%":
        return op1 % op2
    elif op == "sqrt":
        if op1 < 0:
#          print(complex(0, op1*(-1)))
          return complex(0, math.sqrt(op1*(-1)))
        return math.sqrt(op1)
    elif op == "^":
        return op1 ** op2
    elif op == "sin":
        return math.sin(math.radians(op1))
    elif op == "cos":
        return math.cos(math.radians(op1))
    elif op == "tan":
        return math.tan(math.radians(op1))
    elif op == "sinr":
        return math.sin(op1)
    elif op == "cosr":
        return math.cos(op1)
    elif op == "tanr":
        return math.tan(op1)


def getAnswer(mystring):
    x = tempmath(mystring)
    print(x)
    return str(x)
        
class CalcGridLayout(GridLayout):

    def calculate(self, calculation):
        if calculation:
          try:
            self.display.text = str(getAnswer(calculation))
          except Exception:
            self.display.text = "Error"

    def linkopen(self):
      webbrowser.open('https://imcrazybuild.blogspot.com/')

    def optionate(self, entry, option1, option2, option3, option4, slider):
      if entry:
        try:
          if(entry == option1):
            x = 1
          elif(entry == option2):
            x = 2
          elif(entry == option3):
            x = 3
          elif(entry == option4):
            x = 4
          return str(x)
        except Exception:
          pass
        try:
          option1 = str(eval(option1))
          option2 = str(eval(option2))
          option3 = str(eval(option3))
          option4 = str(eval(option4))
          soln1 = (float(entry)-float(option1))+slider
          soln2 = (float(entry)-float(option2))+slider
          soln3 = (float(entry)-float(option3))+slider
          soln4 = (float(entry)-float(option4))+slider
          list1 = [soln1, soln2, soln3, soln4]
          choice =  str(1+list1.index(min(list1, key=lambda x:abs(x-100))))
          return choice
        except Exception:
          return "Error"

class AptitudeSolverApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = AptitudeSolverApp()
calcApp.run()
