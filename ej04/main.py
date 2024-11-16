# ej04: Height and Width

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1
        self.row_force_default=True
        self.row_default_height=120
        self.col_force_default=True
        self.col_default_width=100
        
        self.top_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100
            )
        self.top_grid.cols = 2

        self.name = TextInput(multiline=False)
        self.pizza = TextInput(multiline=False)
        self.color = TextInput(multiline=False)
        self.submit = Button(
            text="Submit",
            font_size=32,
            size_hint_y=None, # que no se ajuste automaticamente, se definirá con height
            height=50,
            size_hint_x=None,
            width=200
            )
        self.submit.bind(on_press=self.press)

        self.top_grid.add_widget(Label(text="Name: "))
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))
        self.top_grid.add_widget(self.pizza)
        self.top_grid.add_widget(Label(text="Favorite Color: "))
        self.top_grid.add_widget(self.color)
        
        self.add_widget(self.top_grid)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza, and your fav color is {color}!"))

class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == "__main__":
    MyApp().run()