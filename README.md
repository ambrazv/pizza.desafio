# Proyecto de Pizza en Python

Este proyecto implementa una clase `Pizza` que permite realizar pedidos personalizados, validando los ingredientes seleccionados.
Archivos

- **pizza.py**: Define la clase `Pizza`.
- **ingredientes.py**: Contiene las listas de ingredientes permitidos.
  Uso

Acceso a Atributos de Clase

```python
from pizza import Pizza
print('Precio:', Pizza.precio)
print('Tamaño:', Pizza.tamano)
```

Validación de Ingredientes

```python
es_valido = Pizza.validar_elemento('salsa de tomate', ['salsa de tomate', 'salsa bbq'])
print(f'¿\'salsa de tomate\' está en la lista? {es_valido}')
```

Crear y Validar una Pizza

```python
mi_pizza = Pizza()
mi_pizza.realizar_pedido()
print('¿Es una pizza válida?', mi_pizza.pizza_valida)
print('Ingredientes:', mi_pizza.ingredientes_vegetales)
print('Proteína:', mi_pizza.ingrediente_proteico)
print('Masa:', mi_pizza.tipo_masa)
```

Requisitos
Python 3.x
Ejecución
Clona el repositorio y ejecuta el script principal:

```bash
python main.py
```

Licencia
Este proyecto está bajo la licencia MIT.
