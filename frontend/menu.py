from tabulate import tabulate  
from frontend.vistas import (
    mostrar_productos,
    formulario_crear_producto,
    formulario_editar_producto,
    formulario_eliminar_producto
)
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
        print("\n=== SISTEMA DE GESTIÓN DE PRODUCTOS ===")
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar todos los productos")
        print("2. Buscar producto por ID")
        print("3. Crear nuevo producto")
        print("4. Editar producto existente")
        print("5. Eliminar producto")
        print("6. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            clear_screen()
            mostrar_productos()  
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            clear_screen()
            buscar_producto()
        elif opcion == "3":
            formulario_crear_producto()
        elif opcion == "4":
            formulario_editar_producto()
        elif opcion == "5":
            formulario_eliminar_producto()
        elif opcion == "6":
            clear_screen()
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("\nPresione Enter para continuar...")

def init():
    if __name__ == "__main__":
        mostrar_menu()