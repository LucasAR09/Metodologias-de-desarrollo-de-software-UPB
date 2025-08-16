from backend.hoja_producto import obtenerHojaDeProductos
from backend.excel import guardarHoja

hoja = obtenerHojaDeProductos()

def listarProductos():
    filas = []
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)

    for refFila in refFilas:
        valores = []
        for celda in refFila:
            valores.append(celda.value)
        filas.append(valores)

    return filas

def consultarProducto(id_producto, soloValores=True):
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if refFila[0].value == id_producto:
            if soloValores:
                valores = [idx]
                for celda in refFila:
                    valores.append(celda.value)
                return valores
            else:
                return refFila
    return None

def crearProducto(Id, Nombre, Precio, Cantidad):
    if consultarProducto(Id) is not None:
        return False
    
    producto = (Id, Nombre, Precio, Cantidad)
    hoja.append(producto)
    guardarHoja(hoja)
    
    return True    

def eliminarProducto (Id):
    producto = consultarProducto(Id)

    if producto == None:
        return False
    
    hoja.delete_rows(producto[0]+2)

    guardarHoja(hoja)

    return True

def actualizarProducto(Id, Nombre, Precio, Cantidad):
    nuevos_valores = (Id, Nombre, Precio, Cantidad)

    refFila = consultarProducto(Id, False)

    if refFila == None:
        return False
    
    for celda, nuevos_valor in zip(refFila, nuevos_valores):
        celda.value = nuevos_valor

    guardarHoja(hoja)

    return True