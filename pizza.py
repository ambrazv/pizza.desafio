"""
Clase Pizza para realizar pedidos y validaciones de pizzas.

Atributos de clase:
    precio (int): Precio fijo para todas las pizzas.
    tamano (str): Tamaño fijo para todas las pizzas.

Atributos de instancia:
    ingrediente_proteico (str): El ingrediente proteico seleccionado por el usuario.
    ingredientes_vegetales (list): Lista de ingredientes vegetales seleccionados por el usuario.
    tipo_masa (str): El tipo de masa seleccionado por el usuario.
    pizza_valida (bool): Indicador de si la pizza es válida o no según los ingredientes y tipo de masa seleccionados.

Métodos:
    __init__(): Inicializa una instancia de la clase Pizza con valores predeterminados.
    
    validar_elemento(elemento, valores_posibles):
        Valida si el elemento proporcionado está en la lista de valores posibles.
    
    realizar_pedido():
        Solicita al usuario los detalles de la pizza, incluyendo el ingrediente proteico,
        los ingredientes vegetales y el tipo de masa. Valida los elementos seleccionados
        y establece si la pizza es válida o no.
"""

from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipos_masa


class Pizza:
    precio = 10000  # Precio fijo para todas las pizzas
    tamano = "familiar"  # Tamaño fijo para todas las pizzas

    def __init__(self):
        self.ingrediente_proteico = ""
        self.ingredientes_vegetales = []
        self.tipo_masa = ""
        self.pizza_valida = False

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        """Valida si el elemento está en la lista de valores posibles."""
        return elemento in valores_posibles

    def realizar_pedido(self):
        """Solicita al usuario los ingredientes y tipo de masa, y valida la pizza."""
        print("Por favor, ingresa los detalles de la pizza:")

        proteico = input(
            "Ingresa el ingrediente proteico (pollo, vacuno, carne vegetal): "
        )
        vegetal1 = input(
            "Ingresa el primer ingrediente vegetal (tomate, aceitunas, champiñones): "
        )
        vegetal2 = input(
            "Ingresa el segundo ingrediente vegetal (tomate, aceitunas, champiñones): "
        )
        masa = input("Ingresa el tipo de masa (tradicional, delgada): ")

        self.ingrediente_proteico = proteico
        self.ingredientes_vegetales = [vegetal1, vegetal2]
        self.tipo_masa = masa

        # Validar los ingredientes y el tipo de masa
        if (
            Pizza.validar_elemento(proteico, ingredientes_proteicos)
            and Pizza.validar_elemento(vegetal1, ingredientes_vegetales)
            and Pizza.validar_elemento(vegetal2, ingredientes_vegetales)
            and Pizza.validar_elemento(masa, tipos_masa)
        ):
            self.pizza_valida = True
        else:
            self.pizza_valida = False
