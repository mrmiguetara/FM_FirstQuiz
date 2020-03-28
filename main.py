"""
Ejercicios adicionales de la clase #1
"""
# 1.
# Dado el string: “Hi there Sam!”
# split el string en cada variable y luego haz una lista


def ejercicio_adicional_1():
    greeting = "Hi there Sam!"
    list_of_words = greeting.split(' ')
    print(f"Resultado ejercicio adicional 1. {list_of_words}")


# Dadas las variables:
# planet = "Earth"
# diameter = 12742
# Usa .format() para print el siguiente string:
# The diameter of Earth is 12742 kilometers.


def ejercicio_adicional_2():
    planet = "Earth"
    diameter = 12742
    print("The diameter of {0} is {1} kilometers.".format(
        planet,
        diameter
    ))


# Dada la siguiente lista nested, usa index para sacar la palabra hello
# lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


def ejercicio_adicional_3():
    lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
    hello = lst[3][1][2][0]
    print(hello)


"""
==============================================================================
Ejercicios del quiz
==============================================================================
"""

# ==============================================================================
# 1. Crea un string con tu nombre y apellido, luego separalo y dale un formato.
full_name = "Miguel Gonzalez"
first_name, last_name = full_name.split(' ')
print("{0}, {1}".format(last_name, first_name))
# ==============================================================================


# ==============================================================================
# 2. Crea un diccionario llamado diccionario_1, con 5 variables
diccionario_1 = {
    'centimetro': 0.01,
    'metro': 1,
    'decametro': 10,
    'kilometro': 1_000,
    'megametro': 1_000_000,
}
# ==============================================================================


# ==============================================================================
# 3. Elige un valor del diccionario creado anteriormente. LLama la variable valor_1.
valor_1 = diccionario_1['centimetro']
# ==============================================================================


# ==============================================================================
# 4. Agrega una variable a diccionario_1
diccionario_1['milimetro'] = 0.001
# ==============================================================================


# ==============================================================================
# 5. Crea un diccionario vacio llamado diccionario_2
diccionario_2 = {}
# ==============================================================================


# ==============================================================================
# 6. Agrega una variable a diccionario_2, cámbiala y luego bórrala
diccionario_2['algo'] = 25
diccionario_2['algo'] = 50
del diccionario_2['algo']
# ==============================================================================


# ==============================================================================
# 7. Crea un tuple con 5 ciudades
cities = ('Santo Domingo', 'New York', 'Miami', 'San Francisco', 'Santiago')
# ==============================================================================


# ==============================================================================
# 8. Crea una lista de 5 ciudades llamada city y luego aplicale el comando for
city = ['Santo Domingo', 'New York', 'Miami', 'San Francisco', 'Santiago']
for c in city:
    print(c)
# ==============================================================================


# ==============================================================================
# 9. Utiliza comandos if, else y elif en la lista city para clasificar las ciudades
# por la primera letra de su nombre
for c in city:
    if c[0] == 'S':
        print('Super city')
    elif c[0] == 'M':
        print('Medium city')
    else:
        print('Small city')
# ==============================================================================


# ==============================================================================
# 10. Crea un código utilizando un while loop de la lista city
index = 0
while index < 5:
    print(city[index])
# ==============================================================================


# ==============================================================================
# 11. Quita 2 valores de la lista city
del city[0]
del city[1]
# ==============================================================================


# ==============================================================================
# 12. Utiliza el comando for en una llave de un diccionario con el nombre de tu
# preferencia
diccionario_1['iter'] = ['h', 'e', 'l', 'l', 'o']
for el in diccionario_1['iter']:
    # do something
    pass
# ==============================================================================


# ==============================================================================
# 13. Tienes una lista de diccionarios llamada customers(clientes),
# con las variables: id, first_name, last_name, address:
# a) Busca la dirección del cliente 2870
# b) Agrega el cliente (customer) 2871 con first_name, last_name y address de tu preferencia
# c) Modifica el first name anteriormene ingresado
# d) Borra el cliente 2871

# declaring a dict for IDE purposes
customers = []

# a)
desire_customer = {}
for customer in customers:
    if customer['id'] == 2870:
        desire_customer = customer
        break

# b)
customers.append({
    'id': 2870,
    'first_name': 'Miguel',
    'last_name': 'Gonzalez',
    'address': 'Paseo Sevilla #27, Puerta de Hierro'
})

# c)
customers[-1]['first_name'] = 'Alejandro'

# d)
del customers[-1]
# ==============================================================================


# ==============================================================================
# 14. Crea 3 funciones y muéstralas
def func1():
    pass


def func2():
    pass


def func3():
    pass


print(func1, func2, func3)
# ==============================================================================


# ==============================================================================
# 15. Realiza 3 comandos utilizando modulos
a = 5 % 2
b = 2 % 1
c = a % 2 == 0
# ==============================================================================
