nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]


notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]


def generar_diccionario(nombres, notas1,notas2):
    """Esta funcion recibe un texto y dos listas y genera un diccionario, usando como clave el nombre del alumno
    y como valor  una tupla con dos elementos(sus dos notas)"""
    nombres=[nombre.strip() for nombre in nombres.split(",")]
    alumnos={} 
    for nombre,nota1,nota2 in zip(nombres,notas1,notas2):
        alumnos[nombre]=(nota1,nota2)
    return alumnos


def obtener_promedios(estructura_de_datos):
    """Esta funcion calcula el promedio de cada alumno usando lambda y con
    map aplica esa funcion a cada elemento de la estructura de datos y devuelve una lista con dichos promedios"""
    prom=map(lambda x:(x[0]+x[1])/2,estructura_de_datos.values())
    return list(prom)

def obtener_promedio_general(lista_de_promedios):
    """Esta funcion calcula y retorna  el promedio de todos los alumnos"""
    prom=0
    if ( len(lista_de_promedios) > 0):
       prom=sum(lista_de_promedios)/ len(lista_de_promedios) 
    return prom


def obtener_promedio_mas_alto(lista_de_promedios,nombres):
    """esta funcion recibe la lista de promedios y un texto, y retorna el nombre y su promedio correspondiente
    del alumno que tiene el promedio mas alto"""
    indice=lista_de_promedios.index(max(lista_de_promedios))
    nombre= nombres.split(",")[indice]
    return nombre,lista_de_promedios[indice]


def obtener_promedio_mas_bajo(lista_de_promedios,nombres):
    """esta funcion recibe la lista de promedios y un texto, y retorna el nombre y su promedio correspondiente
    del alumno que tiene el promedio mas bajo"""
    indice=lista_de_promedios.index(min(lista_de_promedios))
    nombre= nombres.split(",")[indice]
    return nombre,lista_de_promedios[indice],
print()
print("-----------------------------------DICCIONARIO-------------------------------------")
print()


estructura_de_datos=generar_diccionario(nombres,notas_1,notas_2)

print(estructura_de_datos)
print()
lista_de_promedios=obtener_promedios(estructura_de_datos)
prom_general=obtener_promedio_general(lista_de_promedios)

print(f"LISTA DE PROMEDIOS {lista_de_promedios}")
print(f"El promedio general de todos los alumnos es de {prom_general} ")
prom_max=obtener_promedio_mas_alto(lista_de_promedios,nombres)
prom_min=obtener_promedio_mas_bajo(lista_de_promedios,nombres)

print(f"El alumno con promedio mas alto es{prom_max[0]}, con un promedio de {prom_max[1]}")
print(f"El alumno con promedio mas bajo es{prom_min[0]}, con un promedio de {prom_min[1]}")
