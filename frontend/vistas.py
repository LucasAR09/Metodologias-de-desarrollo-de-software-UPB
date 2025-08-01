from tabulate import tabulate
from backend.producto import listarProductos
from utils.limpiar import clear_screen 

def mostrar_productos():
    productos = listarProductos()
    headers = ["ID", "Nombre", "Precio", "Cantidad"]
    
    print("\n--- LISTADO DE PRODUCTOS ---")
    print(tabulate(productos, headers=headers, tablefmt="grid"))
    print("\nNota: Los IDs de productos comienzan con 'P' (ej: P001, P002)")