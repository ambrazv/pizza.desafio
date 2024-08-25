# Proyecto de Pizza en Python

Este proyecto implementa una clase `Pizza` que permite realizar pedidos personalizados, validando los ingredientes seleccionados.
Archivos

- **pizza.py**: Define la clase `Pizza`.
- **ingredientes.py**: Contiene las listas de ingredientes permitidos.
  Uso

## Acceso a Atributos de Clase

```python
from pizza import Pizza
print('Precio:', Pizza.precio)
print('Tamaño:', Pizza.tamano)
```

## Validación de Ingredientes

```python
es_valido = Pizza.validar_elemento('salsa de tomate', ['salsa de tomate', 'salsa bbq'])
print(f'¿\'salsa de tomate\' está en la lista? {es_valido}')
```

## Crear y Validar una Pizza

```python
mi_pizza = Pizza()
mi_pizza.realizar_pedido()
print('¿Es una pizza válida?', mi_pizza.pizza_valida)
print('Ingredientes:', mi_pizza.ingredientes_vegetales)
print('Proteína:', mi_pizza.ingrediente_proteico)
print('Masa:', mi_pizza.tipo_masa)
```

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instalado:

- **Sistema Operativo:** Windows, Linux, macOS
- **Lenguaje de programación:** Python 3.12 o superior

## Instalación del Proyecto

1. **Clona el repositorio:**

   ```bash
   git clone git@github.com:ambrazv/pizza.desafio.git
   ```

2. **Accede al directorio del proyecto:**

   ```bash
   cd pizza.desafio
   ```

## Instrucciones para Ejecutar el Proyecto

1. **Ejecuta el script principal:**

   ```bash
   evaluaciones.py
   ```

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo `LICENSE.md` para más detalles.
