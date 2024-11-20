from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('button_image.kv')

class MyLayout(Widget):
    def hello_on(self):
        self.ids.my_label.text = "Button Clicked, Hello!"
        self.ids.my_image.source = "./images/button_on.png"
    
    def hello_off(self):
        self.ids.my_label.text = "Click the Button"
        self.ids.my_image.source = "./images/button_off.png"

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()