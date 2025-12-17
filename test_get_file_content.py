from functions.get_file_content import get_file_content


# --- Ejecución Individual ---

print("--- Ejecutando Primera Llamada: main.py ---")
try:
    # Si esta falla, solo se detiene este bloque
    print(get_file_content("calculator", "main.py"))
except ValueError as e:
    print(e)

print("\n--- Ejecutando Segunda Llamada: 'pkg/calculator.py' ---")
try:
    # Se ejecuta incluso si la anterior falló
    print(get_file_content("calculator", "pkg/calculator.py"))
except ValueError as e:
    print(e)

print("\n--- Ejecutando Tercera Llamada: '/bin/cat' ---")
try:
    print(get_file_content("calculator", "/bin/cat"))
except ValueError as e:
    print(e)
    
print("\n--- Ejecutando Cuarta Llamada: pkg/does_not_exist.py ---")
try:
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
except ValueError as e:
    print(e)

print("\n--- Fin de la Ejecución ---")
