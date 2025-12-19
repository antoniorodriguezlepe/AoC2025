file_path = "./dia2-test.txt"

with open(file_path, 'r', encoding='utf-8') as f:
	line = f.readline().strip()

values = [v.strip() for v in line.split(',')] if line else []

print(values)
