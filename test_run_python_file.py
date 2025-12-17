from functions.run_python_file import run_python_file

print("--- Iniciando Ejecución ---")

try:
    print("\n[Llamada 1: main.py sin args]")
    resultado = run_python_file("calculator", "main.py")
    print(resultado)
except Exception as e:
    print(f"ERROR CAPTURADO: {e}")


try:
    print("\n[Llamada 2: main.py con '3 + 5']")
    resultado = run_python_file("calculator", "main.py", ["3 + 5"])
    print(resultado)
except Exception as e:
    print(f"ERROR CAPTURADO: {e}")


try:
    print("\n[Llamada 3: tests.py]")
    resultado = run_python_file("calculator", "tests.py")
    print(resultado)
except Exception as e:
    print(f"ERROR CAPTURADO: {e}")


try:
    print("\n[Llamada 4: '../main.py' - Debería fallar]")
    resultado = run_python_file("calculator", "../main.py")
    print(resultado)
except Exception as e:
    print(f"ERROR CAPTURADO: {e}")


try:
    print("\n[Llamada 5: 'nonexistent.py' - Debería fallar]")
    resultado = run_python_file("calculator", "nonexistent.py")
    print(resultado)
except Exception as e:
    print(f"ERROR CAPTURADO: {e}")


try:
    print("\n[Llamada 6: 'lorem.txt' - Debería fallar]")
    resultado = run_python_file("calculator", "lorem.txt")
    print(resultado)
except Exception as e:
    print(f"ERROR CAPTURADO: {e}")

print("\n--- Ejecución finalizada ---")