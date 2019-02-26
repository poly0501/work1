#python Desktop\PYTHON\lekzuu\DZ1.py
#EASY-3
print("EASY-3")
v = int(input("Введите свой возраст:"))
if v >= 18:
    print("Доступ разрешён")
else:
    print("Извините, пользование данным ресурсом только с 18 лет")

#NORMAL-1
print("\nNORMAL-1")
t = int(input("Введите число:"))
max = 0
while  t != 0:
    if (t % 10) >= max:
        max = t % 10
        t = t // 10 
    else:
        t = t // 10
print(max)

#NORMAL-2
print("\nNORMAL-2")
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))

a, b = b, a 


print(a,b)

#NORMAL-3
print("\nNORMAL-3")
import math
print("ax^2+bx+c=0")
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
D = b ** 2 + 4 * c * a
x1 = (-b + math.sqrt(D)) / (2 * a)
x2 = (-b - math.sqrt(D)) / (2 * a)
print(x1,x2)


#HARD-1
print("\nHARD-1")
N = int(input("Введите число:"))
c = 0
for i in range(2,N - 1):
    if N % i == 0:
	    c = 7
	    c = c + 1
print(c)
if c == 0:
    print("Число", N, "простое")
else:
    print("Число",N, "непростое")
	
#HARD-2
print("\nHARD-2")
K = int(input("Введите число:"))
o = 0
p = 1
for j in range(1,K - 1):
    Fib = o + p
    o = p
    p = Fib
print("Фибаначи",Fib)


#HARD-3
print("\nHARD-3")
n = int(input("Введите количество строк:"))
m = int(input("Введите количество AAA:"))
A = "AAABBB"
B = "BBBAAA"
A = A * m
B = B * m 

if n % 2 != 0:
    print(A)
    n = n // 2
    for i in range(n):
        print(B)
        print(A)
        n = n - 1
else:
    n = n // 2
    for i in range(n):
        print(A)
        print(B)
        n = n - 1