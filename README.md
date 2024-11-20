# Tutorial Kivy

- Fuente: Codemy.com: <https://www.youtube.com/playlist?list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg>

Índice
<!-- TOC -->

- [Tutorial Kivy](#tutorial-kivy)
    - [Instalación](#instalaci%C3%B3n)
    - [Uso de librerías](#uso-de-librer%C3%ADas)
    - [Ejemplo de uso](#ejemplo-de-uso)
- [Conceptos](#conceptos)
    - [Widgets](#widgets)
    - [Layouts Diseño](#layouts-dise%C3%B1o)
    - [Arquitectura de una Aplicación](#arquitectura-de-una-aplicaci%C3%B3n)
    - [Eventos y Propiedades](#eventos-y-propiedades)
    - [Archivos .kvv](#archivos-kvv)
- [Ejercicios](#ejercicios)

<!-- /TOC -->

## Instalación

1. Crear carpeta de proyecto:

```sh
mkdir kivy-tutorial
```

2. Instalar librería kivy

```sh
pip install kivy
```

## Uso de librerías

Al comenzar un proyecto, importar las siguiente librerías

```python
import kivy # necesario
from kivy.app import App # necesario
from kivy.uix.label import Label # opcional, trae la widget Label
```

## Ejemplo de uso
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

# Conceptos

## Widgets
Son los elementos fundamentales que se utilizan para construir interfaces de usuario. Es una clase que representa un elemento, puede ser un botón, un cuadro de texto, una etiqueta, un control deslizante, entre otros

1. **Widgets básicos**
    - `Label`: para mostrar texto
    - `Button`: para acciones al hacer click
    - `TextInput`: para ingresar texto
    - `CheckBox`: para opciones seleccionables
    - `Slider`: para seleccionar un valor dentro de un rango
    - `Switch`: un interruptor de encendido/apagado
    - `Image`: para mostrar imágenes

## Layouts (Diseño)
Los layouts definen cómo se organizan y posicionan los widgets dentro de la ventana de la aplicación

**Ejemplos**

- `BoxLayout`: organiza widgets en una fila o columna
- `GridLayout`: Organiza widgets en una cuadrícula
- `StackLayout`: Apila widgets uno encima del otro
- `AnchorLayout`: Coloca widgets en una posición específica del contenedor
- `FloatLayout`: Posiciona widgets usando coordenadas absolutas


## Arquitectura de una Aplicación
Toda aplicación de Kivy tiene una estructura clara que incluye:

1. **Clase de la aplicación (App):** Es el punto de entrada de la aplicación 
2. **Método `build()`:** Define el widget raíz de la interfaz
3. **Bucle de eventos:** Administra la interacción entre el usuario y la interfaz

## Eventos y Propiedades
Los eventos son fundamentales para capturar interacciones del usuario

- **Eventos predeterminados:** Como `on_press` o `on_text`
- **Eventos personalizados:** Creados mediante código

En Kivy, las propiedades como `text`, `value` o `color` son observables. Al cambiar, pueden desencadenar acciones

## Archivos .kvv`
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

- [x] **Ej01:** Hello World app
- [x] **Ej02:** Boxes and Buttons
- [x] **Ej03:** Layouts
- [x] **Ej04:** Height and Width
- [x] **Ej05:** `.kv` Files
- [x] **Ej06:** Kivy builder
- [x] **Ej07:** Changing Kivy Button Colors
- [x] **Ej08:** Python Box Layout
- [x] **Ej09:** Setting Default Widget Properties
- [x] **Ej10:** Change Background Color and Text Color of Labels
- [x] **Ej11:** Two Ways to Change Background Colors
- [x] **Ej12:** How to use Images with Kivy
- [x] **Ej13:** Kivy Float Layout
- [x] **Ej14:** How to Update Labels
- [x] **Ej15:** Build a Simple Calculator App
- [x] **Ej16:** Calculator Addition Function
- [x] **Ej17:** Secondary Calculator Button Functions
- [x] **Ej18:** Fix Our Decimal Calculator Problem
- [x] **Ej19:** Math Calculator Buttons With `eval()`
- [ ] **Ej20:** Standalone Python EXE Executable
- [ ] **Ej21:** Kivy 2.0
- [x] **Ej22:** How to Create Rounded Buttons with Kivy
- [x] **Ej23:** Image Viewer with `FileChooserIconView` and `FileChooserListView`
- [x] **Ej24:** Spell Checker with Kivy
- [x] **Ej25:** Sliders for Kivy
- [x] **Ej26:** Accordions for Kivy
- [x] **Ej27:** Carousels for Kivy
- [x] **Ej28:** How to create Checkboxes with Kivy
- [x] **Ej29:** How to create buttons for Kivy
- [x] **Ej30:** How to create Popup Boxes for Kivy
- [ ] **Ej31:** Multiple Windows with `ScreenManager`
- [ ] **Ej32:** Spinner Dropdowns
- [ ] **Ej33:** How to resize Widgets with Splitters
- [ ] **Ej34:** How to create Tabs in Kivy
- [ ] **Ej35:** How to use Images as Buttons in Kivy
- [ ] **Ej36:** How to Create Animation with Kivy
- [ ] **Ej37:** How to create Progress Bars with Kivy
- [ ] **Ej38:** How to use Markup to change Text Style
- [ ] **Ej39:** How to create a Switch with Kivy
- [ ] **Ej40:** Intro to KivyMD Installation
- [ ] **Ej41:** How to teach yourself KivyMD quickly
- [ ] **Ej42:** Which is better Kivy or Tkinter?
- [ ] **Ej43:** Using Color Themes for KivyMD
- [ ] **Ej44:** Creating a Login Screen with KivyMD
- [ ] **Ej45:** Create a Bottom Bar Button with KivyMD
- [ ] **Ej46:** Navbar with Icons, with KivyMD
- [ ] **Ej47:** Speed Dial Button Menu widh KivyMD
- [ ] **Ej48:** Alert Dialog Boxes for KivyMD
- [ ] **Ej49:** Build and Image Swiper App for KivyMD
- [ ] **Ej50:** Image Swiper App Tricks and Tips
- [ ] **Ej51:** KivyMD Date Picker
- [ ] **Ej52:** KivyMD Time Picker
- [ ] **Ej53:** KivyMD DataTables
- [ ] **Ej54:** KivyMD Pagination for Data Tables
- [ ] **Ej55:** Using SQLite3 Databases with Kivy
- [ ] **Ej56:** Using MySQL Database with Kivy
- [ ] **Ej57:** Using Postgres Database with Kivy
- [ ] **Ej58:** Remove Titlebar from Kivy App
- [ ] **Ej59:** Add Matplotlib Graph to Kivy
- [ ] **Ej60:** Add a Map to your Kivy App
- [ ] **Ej61:** Using Python Code ond a `.kv` Design File
- [ ] **Ej62:** Add Keyboard with `VKeyboard`
- [ ] **Ej63:** Build a TicTacToe Game Logic Part1
- [ ] **Ej64:** Build a TicTacToe Game Logic Part2
- [ ] **Ej65:** Build a TicTacToe Game Logic Part3