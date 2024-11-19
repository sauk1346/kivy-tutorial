from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.spelling import Spelling


Builder.load_file('spell.kv')

class MyLayout(Widget):
    def press(self):
        s = Spelling()
        s.select_language('en_US')

        word = self.ids.word_input.text
        options = s.suggest(word)
        x = ""
        for item in options:
            x = f'{x}\n{item}'
        
        self.ids.word_label.text = f'{x}'

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()