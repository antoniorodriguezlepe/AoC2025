file_path = "./dia1.txt"
direccion = "0"
total = 0
valor = 0
dial = 50
with open(file_path, 'r') as file:
    for line in file:
        direccion = line[0]
        valor = int(line[1:].strip())
        if direccion == "R":
            total += (dial + valor) // 100
            dial = (dial + valor) % 100
        elif direccion == "L":
            distancia_ajustada = (100 - dial) % 100
            total += (valor + distancia_ajustada) // 100
            dial = (dial - valor) % 100
    print(total)