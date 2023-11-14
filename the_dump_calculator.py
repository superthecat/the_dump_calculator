
#plugins
from colorama import init
from colorama import Fore, Back, Style

#welcome
print(Fore.GREEN)
print("welcome to the dump calculator ver 0.1")
print(Fore.RESET)
name = input("what's your name? ")

age = input("what's your age? ")

print(f"hello {name} age {age}")

#math
print(Fore.RED)
print("supported operations (+,-,*,/,%,**,//)")
print(Fore.RESET)
what = input("please select operation: ")
print(Back.GREEN+Fore.BLACK)
a = input("number a: ")
print(Back.RESET,Back.BLUE)
b = input("number b: ")
print(Fore.RESET+Back.RESET)

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
print(Fore.RESET,Fore.CYAN)
input (f"press enter to finish {name} ")