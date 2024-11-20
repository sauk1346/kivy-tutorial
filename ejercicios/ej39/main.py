from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


Builder.load_file('switch.kv')

class MyLayout(Widget):
    def switch_click(self, switchObjetc, switchValue):
        if switchValue:
            self.ids.my_label.text = "You Clicked the switch On!"
        else:
            self.ids.my_label.text = "You Clicked the switch Off!"


class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()