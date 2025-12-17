from functions.write_file import write_file

print("--- Ejecutando Primera Llamada: lorem.txt ---")
try:
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
except ValueError as e:
    print(e)

print("\n--- Ejecutando Segunda Llamada: pkg/morelorem.txt ---")
try:
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
except ValueError as e:
    print(e)


print("\n--- Ejecutando Tercera Llamada: pkg/ ---")
try:
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
except ValueError as e:
    print(e)
