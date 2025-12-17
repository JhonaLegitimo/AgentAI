from functions.get_files_info import get_files_info

# --- Ejecución Individual ---

print("--- Ejecutando Primera Llamada: '.' ---")
try:
    # Si esta falla, solo se detiene este bloque
    print(get_files_info("calculator", "."))
except (FileNotFoundError, ValueError) as e:
    print(e)

print("\n--- Ejecutando Segunda Llamada: 'pkg' ---")
try:
    # Se ejecuta incluso si la anterior falló
    print(get_files_info("calculator", "pkg"))
except (FileNotFoundError, ValueError) as e:
    print(e)

print("\n--- Ejecutando Tercera Llamada: '/bin' ---")
try:
    print(get_files_info("calculator", "/bin"))
except (FileNotFoundError, ValueError) as e:
    print(e)
    
print("\n--- Ejecutando Cuarta Llamada: '../' ---")
try:
    print(get_files_info("calculator", "../"))
except (FileNotFoundError, ValueError) as e:
    print(e)

print("\n--- Fin de la Ejecución ---")