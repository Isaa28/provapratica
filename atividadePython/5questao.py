hora = int(input("Digite uma hora:"))
while hora <0 or hora >23: 
    hora = int(input("Digite uma hora:"))
    if hora <0 or hora >23:
        print("Valor inválido.")
if hora >=0 and hora <12:
    print("Está de manhã.")
if hora >=12 and hora <18:
    print("Está de tarde.")
if hora >=18 and hora <=23:
    print("Está de noite.")
        