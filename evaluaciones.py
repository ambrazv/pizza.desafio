"""
Ejemplo de uso de la clase Pizza.

a. Muestra los valores de los atributos de clase sin crear una instancia.
b. Valida un elemento en una lista usando un método estático.
c. Crea una instancia de Pizza y realiza un pedido.
d. Muestra los detalles de la pizza y su validez.
"""

from pizza import Pizza

# a. Mostrar los valores de los atributos de clase sin crear una instancia
print("Precio de la pizza:", Pizza.precio)
print("Tamaño de la pizza:", Pizza.tamano)

# b. Verificar si "salsa de tomate" está en la lista ["salsa de tomate", "salsa bbq"]
elemento_a_validar = "salsa de tomate"
lista_posibles = ["salsa de tomate", "salsa bbq"]

# Usar el método validar_elemento sin crear una instancia de Pizza
es_valido = Pizza.validar_elemento(elemento_a_validar, lista_posibles)
print(f"¿'salsa de tomate' está en la lista? {es_valido}")

# c. Crear una instancia de la clase Pizza y realizar un pedido
mi_pizza = Pizza()
mi_pizza.realizar_pedido()

# d. Mostrar en pantalla los ingredientes y tipo de masa, y si es una pizza válida
print("¿Es una pizza válida?\n", mi_pizza.pizza_valida)
print("Ingredientes vegetales:", mi_pizza.ingredientes_vegetales)
print("Ingrediente proteico:", mi_pizza.ingrediente_proteico)
print("Tipo de masa:", mi_pizza.tipo_masa)


# e. Mostrar un mensaje sobre la validez de la pizza en la clase (sin crear una instancia)
print()
