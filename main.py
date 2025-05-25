from kivy.app import App
from kivy.uix.label import Label

class HelloApp(App):
    kv_file = None  # <- Add this line to prevent auto kv loading

    def build(self):
        return Label(text="Hello World")

if __name__ == "__main__":
    HelloApp().run()
