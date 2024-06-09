nome = input("Digite o nome do aluno:")
disciplina = input("Digite o nome da disciplina:")
n1 = int(input("Digite a primeira nota:"))
n2 = int(input("Digite a segunda nota:"))
m = (n1+n2)/2
if m <6:
    situação = 'reprovado(a)'
else:
    situação = 'aprovado(a)'
print(f"{nome} está {situação} na disciplina {disciplina}.")