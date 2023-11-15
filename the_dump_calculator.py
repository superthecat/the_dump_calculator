
#plugins
import time
from colorama import init
from colorama import Fore, Back, Style

#welcome
print(Fore.GREEN)
input("welcome to the dump calculator")
print(Fore.RESET)
time.sleep(0.5)
name = input("what's your name? ")
time.sleep(0.5)
age = input("what's your age? ")
time.sleep(0.5)
print(f"hello {name} age {age}")

#math
print(Fore.RED)
print("supported operations (+,-,*,/,%,**,//)")
print(Fore.RESET)
what = input("please select operation: ")
time.sleep(0.5)
print(Back.GREEN,Fore.BLACK)
a = input("number a: ")
print(Back.RESET,Back.BLUE)
b = input("number b: ")
print(Fore.RESET,Back.RESET)

match what:
    case "//":
        c = float(a) // float(b)
        print(a,"//",b,"=", str(c), name)
    case "**":
        c = float(a) ** float(b)
        print(a,"**",b,"=", str(c), name)
    case "+":
        c = float(a) + float(b)
        print(a,"+",b,"=", str(c), name)
    case "-":
        c = float(a) - float(b)
        print(a,"-",b,"=", str(c), name)

    case "*":
        c = float(a) * float(b)
        print(a,"*",b,"=", str(c), name)

    case "/":
        c = float(a) / float(b)
        print(a,"/",b,"=", str(c), name)

    case "%":
        c = float(a) % float(b)
        print(a, "%", b, "=", str(c), name)

    case _what:
        print(Fore.RED)
        print(f"sorry {name} bad selection")
time.sleep(0.5)
print(Fore.RESET,Fore.CYAN)
input (f"press enter to finish {name} ")
