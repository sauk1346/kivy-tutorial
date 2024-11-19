# Tutorial Kivy

- Fuente: Codemy.com: <https://www.youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg>


## 1. Instalación

1. Crear carpeta de proyecto:

```sh
mkdir kivy-tutorial
```

2. Crear entorno para instalar librerías (nombre virt)

```sh
cd kivy-tutorial
python -m venv virt
```

3. Activar entorno

```sh
.\virt\Scripts\activate
```

4. Instalar librería kivy

```sh
pip install kivy
```

## 2. Uso de librerías

Al comenzar un proyecto, importar las siguiente librerías

```python
import kivy # necesario
from kivy.app import App # necesario
from kivy.uix.label import Label # opcional, trae la widget Label
```

## 3. Ejemplo de uso
Programa que muestra en pantalla "Hello World!"

```python
import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello World!")

if __name__ == "__main__":
    MyApp().run()
```

# 3. Conceptos

## 3.1 Widgets
Son los elementos fundamentales que se utilizan para construir interfaces de usuario. Es una clase que representa un elemento, puede ser un botón, un cuadro de texto, una etiqueta, un control deslizante, entre otros

1. **Widgets básicos**
    - `Label`: para mostrar texto
    - `Button`: para acciones al hacer click
    - `TextInput`: para ingresar texto
    - `CheckBox`: para opciones seleccionables
    - `Slider`: para seleccionar un valor dentro de un rango
    - `Switch`: un interruptor de encendido/apagado
    - `Image`: para mostrar imágenes

## 3.2 Layouts (Diseño)
Los layouts definen cómo se organizan y posicionan los widgets dentro de la ventana de la aplicación

**Ejemplos**

- `BoxLayout`: organiza widgets en una fila o columna
- `GridLayout`: Organiza widgets en una cuadrícula
- `StackLayout`: Apila widgets uno encima del otro
- `AnchorLayout`: Coloca widgets en una posición específica del contenedor
- `FloatLayout`: Posiciona widgets usando coordenadas absolutas


## 3.3 Arquitectura de una Aplicación
Toda aplicación de Kivy tiene una estructura clara que incluye:

1. **Clase de la aplicación (App):** Es el punto de entrada de la aplicación 
2. **Método `build()`:** Define el widget raíz de la interfaz
3. **Bucle de eventos:** Administra la interacción entre el usuario y la interfaz

## 3.4 Eventos y Propiedades
Los eventos son fundamentales para capturar interacciones del usuario

- **Eventos predeterminados:** Como `on_press` o `on_text`
- **Eventos personalizados:** Creados mediante código

En Kivy, las propiedades como `text`, `value` o `color` son observables. Al cambiar, pueden desencadenar acciones

## 3.5 Archivos `.kv`
Un archivo `.kv` es una forma declarativa de definir la interfaz gráfica, separando el diseño del código lógico

**Ventajas**
- Claridad, separa la lógica (python) del diseño (KV)
- Reducción de código repetitivo

**Ejemplo**

Archivo KV
```python
BoxLayout
    orientation: "vertical"

    Label:
        text: "Hola mundo!"

    Button:
        text: "Haz click aquí"
```

Vinculación con python
```python
from kivy.app import App
from kivy.uix.boxlayout impor BoxLayout

class MiApp(App):
    def build(self):
        return BoxLayout()
    
    def saludar(self):
        print("Hola mundo!")

if __name__ == "__main__":
    MiApp().run()
```

# Ejercicios

- [x] Ej01: Hello World app
- [x] Ej02: Boxes and Buttons
- [x] Ej03: Layouts
- [x] Ej04: Height and Width
- [x] Ej05: `.kv` Files
- [x] Ej06: Kivy builder
- [x] Ej07: Changing Kivy Button Colors
- [x] Ej08: Python Box Layout
- [x] Ej09: Setting Default Widget Properties
- [x] Ej10: Change Background Color and Text Color of Labels
- [x] Ej11: Two Ways to Change Background Colors
- [x] Ej12: How to use Images with Kivy
- [x] Ej13: Kivy Float Layout
- [x] Ej14: How to Update Labels
- [x] Ej15: Build a Simple Calculator App
- [ ] Ej16: Calculator Addition Function
- [ ] Ej17: Secondary Calculator Button Functions
- [ ] Ej18: Fix Our Decimal Calculator Problem
- [ ] Ej19: Math Calculator Buttons With `eval()`
- [ ] Ej20: Standalone Python EXE Executable
- [ ] Ej21: Kivy 2.0 (old news)
- [ ] Ej22: How to Create Rounded Buttons with Kivy
- [ ] Ej23: Image Viewer with `FileChooserIconView` and `FileChooserListView`
- [ ] Ej24: Spell Checker with Kivy
- [ ] Ej25: Sliders for Kivy
- [ ] Ej26: Accordions for Kivy
- [ ] Ej27: Carousels for Kivy
- [ ] Ej28: How to create Checkboxes with Kivy
- [ ] Ej29: How to create buttons for Kivy
- [ ] Ej30: How to create Popup Boxes for Kivy