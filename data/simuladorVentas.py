import random
from datetime import datetime, timedelta

def generar_ventas(numeroVentas):

    # Productos con los nombres exactos del segundo código
    productos = [
        {"nombre": "Camisa Polo de Hombre Slim Fit Manga Corta con Textura Bordado de Pato en Algodón",
         "precio": 150000, "descuento": False},
        {"nombre": "Camiseta de Hombre Tipo Polo, Classic Fit Manga Corta - Piqué 100% Algodón",
         "precio": 250000, "descuento": False},
        {"nombre": "Camiseta Tipo Polo para Hombre",
         "precio": 200000, "descuento": True},
        {"nombre": "Polo Masculino de Manga Corta en Algodón con Elastano",
         "precio": 230000, "descuento": True},
        {"nombre": "Chaqueta de Mujer, Acolchada - Togs",
         "precio": 500000, "descuento": False},
        {"nombre": "Chaqueta de Mujer Lace Embroidery Look Preppy con C Bordada en Algodón",
         "precio": 600000, "descuento": False},
        {"nombre": "Chaqueta de Mujer en cuero, Silueta Biker - Gamuza",
         "precio": 1500000, "descuento": False},
        {"nombre": "Jean Súper Slim Fit Tiro Bajo Bota Super Slim Azul Oscuro con Rotos para Hombre",
         "precio": 490000, "descuento": True},
        {"nombre": "Jean Súper Slim Fit Tiro Bajo Bota Super Slim Azul Oscuro para Hombre",
         "precio": 357000, "descuento": True},
        {"nombre": "Jean Súper Slim Fit Tiro Bajo Bota Super Slim Azul Claro Lavado Vintage para Hombre",
         "precio": 360000, "descuento": False}
    ]

    tallas = ["XS", "S", "M", "L", "XL", "XXL"]

    vendedores = [
        "julieth tuberquia",
        "sofia tuberquia",
        "ismael ocampo",
        "jessica mora",
        "celeste higuita"
    ]

    fecha_inicio = datetime(2026, 1, 1)
    lista_ventas = []

    for i in range(numeroVentas):
        total_venta = 0
        lista_productos = []
        cantidad_productos = random.randint(1, 3)

        # ✅ Este for está DENTRO del for principal (bug corregido)
        for j in range(cantidad_productos):
            producto = random.choice(productos)
            cantidad_producto = random.randint(1, 5)
            total = producto["precio"] * cantidad_producto

            lista_productos.append({
                "nombre": producto["nombre"],       # ← nombre exacto del catálogo
                "precio": producto["precio"],
                "descuento": producto["descuento"],
                "talla": random.choice(tallas),
                "cantidad": cantidad_producto,
                "total": total
            })
            total_venta += total

        venta = {
            "id": i + 1,
            "vendedor": random.choice(vendedores),
            "productos": lista_productos,
            "total_venta": total_venta,
            "fecha": fecha_inicio + timedelta(days=random.randint(0, 30))
        }
        lista_ventas.append(venta)

    return lista_ventas