hora = int(input("Digite uma hora:"))
while hora <0 or hora >23: 
    hora = int(input("Digite uma hora:"))
    if hora <0 or hora >23:
        print("Valor inválido.")
if hora >=0 and hora <12:
    print("Está de manhã.")
elif hora >=12 and hora <18:
    print("Está de tarde.")
else:
    print("Está de noite.")