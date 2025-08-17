from tabulate import tabulate
from backend.producto import listarProductos, crearProducto, actualizarProducto, eliminarProducto,  consultarProducto 
from utils.limpiar import clear_screen 

def mostrar_productos():
    productos = listarProductos()
    headers = ["ID", "Nombre", "Precio", "Cantidad"]
    
    print("\n--- LISTADO DE PRODUCTOS ---")
    print(tabulate(productos, headers=headers, tablefmt="grid"))
    print("\nNota: Los IDs de productos comienzan con 'P' (ej: P001, P002)")

def formulario_crear_producto():
    clear_screen()
    print("\n--- CREAR NUEVO PRODUCTO ---")
    id_producto = input("Ingrese el ID del producto (ej: P001): ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad en stock: ")
    
    if crearProducto(id_producto, nombre, precio, cantidad):
        print("\n¡Producto creado exitosamente!")
    else:
        print("\nError: Ya existe un producto con ese ID")
    input("\nPresione Enter para continuar...")

def formulario_editar_producto():
    clear_screen()
    print("\n--- EDITAR PRODUCTO ---")
    id_producto = input("Ingrese el ID del producto a editar (ej: P001): ")
    
    producto = consultarProducto(id_producto)
    if not producto:
        print(f"\nError: No se encontró un producto con ID {id_producto}")
        input("\nPresione Enter para continuar...")
        return
    
    print("\nValores actuales:")
    headers = ["ID", "Nombre", "Precio", "Cantidad"]
    print(tabulate([producto[1:]], headers=headers, tablefmt="grid"))
    
    print("\nIngrese los nuevos valores (deje en blanco para mantener el valor actual):")
    nombre = input(f"Nuevo nombre [{producto[1]}]: ") or producto[1]
    precio = input(f"Nuevo precio [{producto[2]}]: ") or producto[2]
    cantidad = input(f"Nueva cantidad [{producto[3]}]: ") or producto[3]
    
    if actualizarProducto(id_producto, nombre, precio, cantidad):
        print("\n¡Producto actualizado exitosamente!")
    else:
        print("\nError al actualizar el producto")
    input("\nPresione Enter para continuar...")

def formulario_eliminar_producto():
    clear_screen()
    print("\n--- ELIMINAR PRODUCTO ---")
    id_producto = input("Ingrese el ID del producto a eliminar (ej: P001): ")
    
    producto = consultarProducto(id_producto)
    if not producto:
        print(f"\nError: No se encontró un producto con ID {id_producto}")
        input("\nPresione Enter para continuar...")
        return
    
    print("\nProducto a eliminar:")
    headers = ["ID", "Nombre", "Precio", "Cantidad"]
    print(tabulate([producto[1:]], headers=headers, tablefmt="grid"))
    
    confirmacion = input("\n¿Está seguro que desea eliminar este producto? (S/N): ").upper()
    if confirmacion == "S":
        if eliminarProducto(id_producto):
            print("\n¡Producto eliminado exitosamente!")
        else:
            print("\nError al eliminar el producto")
    else:
        print("\nOperación cancelada")
    input("\nPresione Enter para continuar...")