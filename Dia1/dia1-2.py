file_path = "./dia1.txt"
direccion = "0"
total = 0
valor = 0
dial = 50
# Open file and read by lines
with open(file_path, 'r') as file:
    for line in file:
        # parse imput into address (L or R) and displacement value
        direccion = line[0]
        valor = int(line[1:].strip())
        if direccion == "R":
            total += (dial + valor) // 100 # Check how many times we pass 0 moving right
            dial = (dial + valor) % 100 # Move right
        elif direccion == "L":
            distancia_ajustada = (100 - dial) % 100 # Calculate how far we are from 0
            total += (valor + distancia_ajustada) // 100 # Check how many times we pass 0 moving left
            dial = (dial - valor) % 100 # Move left
    print(total) # Result