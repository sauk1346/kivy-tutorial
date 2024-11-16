# ej02: boxes and buttons

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        
        self.cols = 2 
        # widgets
        self.name = TextInput(multiline=False)
        self.pizza = TextInput(multiline=False)
        self.color = TextInput(multiline=False)
        self.submit = Button(text="Submit")

        #bind button
        self.submit.bind(on_press=self.press)

        # add widgets to screen
        self.add_widget(Label(text="Name: "))
        self.add_widget(self.name)
        self.add_widget(Label(text="Favorite Pizza: "))
        self.add_widget(self.pizza)
        self.add_widget(Label(text="Favorite Color: "))
        self.add_widget(self.color)
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