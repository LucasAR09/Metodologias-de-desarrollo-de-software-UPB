from backend.excel import obtenerLibro, guardarHoja

libro = obtenerLibro()
titulo_hoja = "productos"

def inicializarHoja():
    hoja = libro.create_sheet(title=titulo_hoja)

    hoja.column_dimensions['A'].width = 10
    hoja.column_dimensions['B'].width = 20
    hoja.column_dimensions['C'].width = 10
    hoja.column_dimensions['D'].width = 10

    cabeceras = ("Id", "Nombre", "Precio", "Cantidad")
    hoja.append(cabeceras)

    guardarHoja(hoja)
    return hoja

def obtenerHojaDeProductos():
    if titulo_hoja in libro.sheetnames:
        return libro[titulo_hoja]
    else:
        return inicializarHoja()
