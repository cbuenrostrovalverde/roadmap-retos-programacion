'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 */
 '''

# Listas, tuplas, conjuntos, diccionarios

# LISTA
verduras = ['tomate', 'lechuga', 'patata']

# Insertar elementos
verduras.append('calabacín')

# Borrar elementos
verduras.remove('tomate')

# Actualizar
verduras[1] = 'berenjena'

# Ordenar
verduras.sort()

print(verduras)

# TUPLA

tupla = (1, 2, 3, 4, 5, 6, 7, 20)

'En una tupla no se pueden modificar los datos'

#   CONJUNTOS

colores = {'rojo', 'amarillo', 'verde', 'azul'}

# Añadir datos al conjunto
colores.add('naranja')

# Borrar pese a que no exista dentro del conjunto
colores.discard('violeta')

# Actualizar datos
colores.update('lo que quieras tú')

# Ordenar (convertirá el conjunto en una lista)
colores_ordenados = sorted(colores)

# DICCIONARIOS

alumnos = {
    'nombre': 'Carlos',
    'edad': 20
}

# Insetar y actualizar datos
alumnos['apellido'] = 'Buenrostro'

alumnos['edad'] = 30

# Eliminar datos

del alumnos['edad']

# Ordenación

sorted_alumnos = dict(sorted(alumnos.items()))
print(alumnos)

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
'''

lista_contactos = []
contactos = {}

def mostrar_menu():
    print("\n--- AGENDA DE CONTACTOS ---")
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Ver todos los contactos")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = int(input('Bienvenido a tu agenda virutal. \n Por favor, escoja una opción: '))
