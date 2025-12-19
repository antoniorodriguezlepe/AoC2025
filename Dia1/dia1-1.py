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
            dial = (dial + valor) % 100
        elif direccion == "L":
            dial = (dial - valor) % 100
        if dial == 0:
            total += 1
    print(total)