a=int(input("enter the first number"))
b=int(input("enter the second number"))
def calculator(a,b):
    sum =a+b
    difference =a-b
    product =a*b
    quotient =a/b
    modulo=a%b

    return sum,difference,product,quotient,modulo
sum , difference ,product ,quotient ,modulo = calculator (a,b)

print("sum:",sum)
print("difference:",difference)
print("product:",product)
print("quotient:",quotient)
print("modulo:",modulo)