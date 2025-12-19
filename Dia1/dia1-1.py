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
        if direccion == "R": # move right
            dial = (dial + valor) % 100
        elif direccion == "L": # move left
            dial = (dial - valor) % 100
        if dial == 0: # Check if final position is at 0
            total += 1
    print(total) # Result