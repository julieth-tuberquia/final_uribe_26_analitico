#crear una funcion que crea Nempleados
#cada empleado tiene:
#id
#nombres y apellidos
#salario base 
#documenmto
#fecha de ingreso a la compañia 

# construir una funcion generadora de N empleados que permite crear MOCKS o datos semilla
# para pruebas o analisis

import random
from datetime import datetime, timedelta

def generar_empleados(numeroEmpleados):

     # simular una lista de vendedores o empleados
     vendedores = [
          "julieth tuberquia",
          "sofia tuberquia",
          "ismael ocampo",
          "jessica mora",
          "celeste higuita"
     ]

     # simular salarios base
     salarios = [1300000,1500000,1800000,2000000]

     # simular fecha de inicio en la empresa
     fechaInicio = datetime(2020,1,1)

     # generar los N empleados que me esten pidiendo
     ListaEmpleados = []

     for i in range(numeroEmpleados):

          nombre = random.choice(vendedores)

          ListaEmpleados.append(
               {
                    "id": i + 1,
                    "nombre": nombre,
                    "salarioBase": random.choice(salarios),
                    "documento": random.randint(1000000000,1099999999),
                    "fechaIngreso": fechaInicio + timedelta(days=random.randint(0,1500))
           
              }
          )
          return ListaEmpleados


    