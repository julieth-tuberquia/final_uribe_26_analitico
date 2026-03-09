  # construir una funcion generadora de N ventas que permite crear MOCKS o datos semilla para la rutina
  # analisis
import random
from datetime import datetime,timedelta

def generar_ventas (numeroVentas):
     #simular una listsa de productos
     productos=[
          {"nombre":"Camisa Polo de Hombre Slim Fit Manga Corta con Textura Bordado de Pato en Algodón",
           "precio":150000,"descuento":False},
          {"nombre":"Camiseta de Hombre Tipo Polo, Classic Fit Manga Corta - Piqué 100% Algodón",
           "precio":250000,"descuento":False},
          {"nombre":"Camiseta Tipo Polo para Hombre",
           "precio":200000,"descuento":True},
          {"nombre":"Polo Masculino de Manga Corta en Algodón con Elastano",
           "precio":230000,"descuento":True},
          {"nombre":"Chaqueta de Mujer, Acolchada - Togs",
           "precio":500000,"descuento":False},
          {"nombre":"Chaqueta de Mujer Lace Embroidery Look Preppy con C Bordada en Algodón",
           "precio":600000,"descuento":False},
          {"nombre":"Chaqueta de Mujer en cuero, Silueta Biker - Gamuza",
           "precio":1500000,"descuento":False},
          {"nombre":"Jean Súper Slim Fit Tiro Bajo Bota Super Slim Azul Oscuro con Rotos para Hombre",
           "precio":490000,"descuento":True},
          {"nombre":"Jean Súper Slim Fit Tiro Bajo Bota Super Slim Azul Oscuro para Hombre",
           "precio":357000,"descuento":True},
          {"nombre":"Jean Súper Slim Fit Tiro Bajo Bota Super Slim Azul Claro Lavado Vintage para Hombre",
           "precio":360000,"descuento":False}
      ]

     # simular una lista  de talla 
     tallas=["XS","S","M","L","XL","XXL"]

     # simular vendedores asociados
     #***********
     vendedores =["julieth tuberquia","sofia tuberquia","ismael ocampo","jessica mora","celeste higuita"]

     # similar la fecha 
     fechaInicio= datetime(2026,1,2)

     #generar la N ventas que me esten pidiendo 
     ventas = []

     for _ in range(numeroVentas):

      numeroProductos = random.randint(1,3)
      listaProductos = []
      totalVenta = 0

     # generar los productos de la venta
     for _ in range(numeroProductos):

          producto = random.choice(productos)
          cantidad = random.randint(1,5)

          totalProducto = cantidad * producto["precio"]

          listaProductos.append(
               {
                    "producto": producto,
                    "precioUnitario": producto["precio"],
                    "talla": random.choice(tallas),
                    "cantidad": cantidad,
                    "total": totalProducto
               }
          )

          totalVenta = totalVenta + totalProducto

     # generar la fecha de la venta
     fecha = fechaInicio + timedelta(days=random.randint(0,60))

     ventas.append(
          {
               "productos": listaProductos,
               "vendedor": random.choice(vendedores),
               "fecha": fecha,
               "totalVenta": totalVenta
          }
     )

     return ventas