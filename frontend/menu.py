from tabulate import tabulate  
from frontend.vistas import mostrar_productos
from backend.producto import consultarProducto  
from utils.limpiar import clear_screen 
import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def buscar_producto():
    id_producto = input("Ingrese el ID del producto a buscar (ej: P001): ")
    producto = consultarProducto(id_producto)
    
    if producto:
        headers = ["ID", "Nombre", "Precio", "Cantidad"]
        print(tabulate([producto[1:]], headers=headers, tablefmt="grid"))
    else:
        print(f"No se encontró ningún producto con ID {id_producto}")
    input("\nPresione Enter para continuar...")

def mostrar_menu():
    while True:
        clear_screen()
        print("\n=== SISTEMA DE PRODUCTOS ===")
        print("\n--- MENÚ DE PRODUCTOS ---")
        print("1. Listar todos los productos")
        print("2. Buscar producto por ID")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            clear_screen()
            mostrar_productos()  
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            clear_screen()
            buscar_producto()
        elif opcion == "3":
            clear_screen()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

def init():
    if __name__ == "__main__":
        mostrar_menu()
