import kivy
kivy.require('1.11.1')  # Set to your Kivy version
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return Builder.load_file('main.kv')


MyApp().run()
