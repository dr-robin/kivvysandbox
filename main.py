import kivy
kivy.require('1.11.1')  # Set to your Kivy version
from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Button(text='Learn')


MyApp().run()
