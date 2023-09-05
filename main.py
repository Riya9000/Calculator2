# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)
        self.calc_field = TextInput(readonly=True, disabled=True, font_size=64, height=200, size_hint=(1, None))
        self.add_widget(self.calc_field)

    def calc_symbol(self, symbol):
        self.calc_field.text += symbol

    def clear(self):
        self.calc_field.text = ""

    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))

class NeuralCalc(App):
    def build(self):
        return MyRoot()

if __name__ == "__main__":
    NeuralCalc().run()
