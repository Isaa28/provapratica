n = int(input("Digite um número para saber a sua tabuada:")) 
x = 1
while x <= 10:
    res = x * n
    print("%d * %d = %d" %(n ,x ,res))
    x += 1