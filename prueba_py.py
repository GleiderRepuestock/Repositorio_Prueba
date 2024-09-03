print("Hello world!")

## TODO: Write your code here
def suma(a, b):
    return a + b


def resta(*args):
    return args


def division(a, b):
    return a / b


def multiplicacion(a, b):
    return a * b

def numerosPares(*args):
    return [i for i in args if i % 2 == 0]



def numerosImpares(*args):
    if len(args) == 0:
        return []
    return [i for i in args if i % 2 != 0]