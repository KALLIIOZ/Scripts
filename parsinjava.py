import os
import re

def search_bluetooth_functions_in_file(java_file):
    bluetooth_functions = []
    with open(java_file, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            # Puedes ajustar esta expresión regular según tus necesidades específicas.
            # En este ejemplo, estamos buscando cualquier referencia a "bluetooth".
            if re.search(r'conections', line, re.IGNORECASE):
                bluetooth_functions.append((java_file, line_number, line.strip()))
    return bluetooth_functions

def search_bluetooth_functions_in_directory(directory):
    bluetooth_functions = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.java'):
                java_file = os.path.join(root, file)
                bluetooth_functions.extend(search_bluetooth_functions_in_file(java_file))
    return bluetooth_functions

if __name__ == "__main__":
    directory_to_search = r"C:\Users\PC\Documents\Programas\LABTDI\LABTDI-main"  # Reemplaza esto con la ruta al directorio que deseas analizar
    bluetooth_functions = search_bluetooth_functions_in_directory(directory_to_search)
    
    if bluetooth_functions:
        print("Referencias a Bluetooth en archivos .java:")
        for func in bluetooth_functions:
            print(f"Archivo: {func[0]}, Línea: {func[1]}, Contenido: {func[2]}")
    else:
        print("No se encontraron referencias a Bluetooth en los archivos .java.")
