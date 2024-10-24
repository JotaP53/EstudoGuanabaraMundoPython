# Usando o exercício para calcular a média do Farias Brito.

v1 = float(input("Digite a nota 1: "))
v2 = float(input("Digite a nota 2: "))

mp = (v1 + v2) / 2

print ("A média parcial do aluno foi: {:.1f}.".format(mp))

v3 = float(input("Digite a nota 3: "))

mf = (mp + v3) / 2

print ("A média final do aluno foi: {:.1f}.".format(mf))
