def funPrints():
    print("Que pasa")

def funPrintFun(prueba):
    print(prueba)

def funPrintConcat(a, b, c = funPrints):
    return str(a) + str(b) + str(c())


fun = funPrints
fun()
print(fun)
fun2 = funPrintFun
fun3 = funPrintFun("aaaa")
fun2("ey")
print(fun2)
print(fun3)
fun4 = funPrintConcat("aaa", fun())
print(fun4)