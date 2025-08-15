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

def consultarProducto(id_producto):
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if refFila[0].value == id_producto:
            valores = [idx]
            for celda in refFila:
                valores.append(celda.value)
            return valores
    else:
        return None

def crearProducto(Id, Nombre, Precio, Cantidad):
    if consultarProducto(Id) is not None:
        return False
    
    producto = (Id, Nombre, Precio, Cantidad)
    hoja.append(producto)
    guardarHoja(hoja)
    
    return True    
