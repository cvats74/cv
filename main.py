from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class Design(BoxLayout):
    

    def change_text(self,inputText):
        inputText.text="by"


class ChatApp(App):
    def build(self):
        return Design()


ChatApp().run()

